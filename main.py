# Cargamos las librerías
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from dotenv import load_dotenv
import os

# Inicializamos
load_dotenv()

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/paraphrase-MiniLM-L6-v2"
)

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    google_api_type="aistudio",
    temperature=0.7
)


def inicializar_vectorstore():
    persist_directory = "chroma_v2/"
    if os.path.exists(persist_directory):
        print("🔄 Cargando vectorstore...")
        return Chroma(persist_directory=persist_directory, embedding_function=embedding_model)

    print("📄 Procesando documentos...")
    loaders = [
        PyPDFLoader("juan_perez_cv.pdf"),
        TextLoader("hoja_de_vida_sin_stopwords.txt")
    ]

    all_docs = []
    for loader in loaders:
        all_docs.extend(loader.load())

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs_divididos = splitter.split_documents(all_docs)

    return Chroma.from_documents(docs_divididos, embedding_model, persist_directory=persist_directory)


def generar_respuesta(pregunta, vectorstore, debug=False):
    # Recuperamos solo los 2 chunks más relevantes, evitando repetición
    retriever = vectorstore.as_retriever(
        search_type="mmr",
        search_kwargs={"k": 2, "fetch_k": 6}
    )
    documentos = retriever.invoke(pregunta)

    # Ver por consola qué fragmentos se usaron
    if debug:
        print("\n🔍 Documentos utilizados:")
        for i, doc in enumerate(documentos, start=1):
            fuente = os.path.basename(doc.metadata.get("source", "desconocido"))
            print(f"\n📄 Documento {i}: {fuente}")
            print(f"📝 Fragmento:\n{doc.page_content[:100]}...")  # Mostramos primeros 100 caracteres

    # Contexto + fuente por documento
    contexto = "\n\n".join(
        f"{doc.page_content}\n\n[Fuente: {os.path.basename(doc.metadata.get('source', 'desconocido'))}]"
        for doc in documentos
    )

    # Obtenemos las fuentes únicas para mostrar al usuario
    fuentes_usadas = sorted(set(os.path.basename(doc.metadata.get('source', 'desconocido')) for doc in documentos))

    prompt = f"""
    Eres el asistente de Juan Pérez.

    Información del perfil profesional:
    {contexto}

    Instrucciones:
    - Usá solo la información presente en los documentos.
    - No inventes datos ni completes con supuestos.
    - Si no tenés datos concretos, podés sugerir contactar a Juan por mail: juanperez@email.com.
    - Usá el mismo idioma que la pregunta.

    Pregunta:
    {pregunta}
    """

    respuesta = llm.invoke(prompt).content.strip()
    fuentes_str = ", ".join(fuentes_usadas)

    return respuesta, fuentes_str


# Debug por consola
if __name__ == "__main__":
    vs = inicializar_vectorstore()
    while True:
        pregunta = input("\n👉 Tu pregunta: ")
        if pregunta.lower() in ["salir", "exit"]:
            break
        rta, fuentes = generar_respuesta(pregunta, vs, debug=True)
        print(f"\n💡 Respuesta: {rta}\n\n📄 Fuente: {fuentes}")
