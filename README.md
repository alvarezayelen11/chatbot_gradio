# 🤖 Asistente Virtual de Juan Pérez

Este proyecto constituye una versión alternativa del proyecto [chatbot_rags](https://github.com/alvarezayelen11/chatbot_rags) alojado en este mismo repositorio.

Al igual que el otro proyecto, se trata de un **asistente virtual** que responde preguntas acerca del perfil profesional del personaje ficticio Juan Pérez. 

### 🔁 Similitudes entre ambos proyectos

- Desarrollados en **Python**.
- Procesan documentos para convertirlos en fragmentos semánticos.
- Utilizan **LangChain** como framework de orquestación.
- Generan **embeddings** con modelos de **HuggingFace**.
- Usan **Chroma** como vector store para almacenamiento y recuperación de información.
- Se apoyan en el modelo **Gemini 1.5 Pro** de Google para generar respuestas.
- Permiten interactuar con el CV de Juan Pérez a través de una interfaz conversacional.

### 🔀 Principales diferencias de esta versión

- Utiliza dos fuentes de información: un archivo `.pdf` y otro `.txt`.
- Los documentos utilizados como fuente se le quitaron las stopwords y fueron sometidos a un proceso de lemmatización y stemming.
- Incluye una función de **debug por consola** que muestra de qué documentos se extrajo cada respuesta (no visible en la interfaz web).
- Para realizar búsquedas semánticas emplea el modelo de embeddings `paraphrase-MiniLM-L6-v2`(más orientado a similitud) en lugar del modelo `all-MiniLM-L6-v2` (más general).
- No tiene configurada la memoria conversacional, mientas que la otra versión recuerda las 3 últimas interacciones. 
- Puede ejecutarse mediante una **interfaz web con Gradio**, mientras que el otro modelo hace lo propio con **Stremlit**.
- Utiliza temperature=0.7 para respuestas menos deterministas.

---

## 📦 Instalación

1. Cloná el repositorio:

```bash
git clone https://github.com/tu-usuario/chatbot_gradio.git
cd chatbot_gradio
```

2. Activá un entorno virtual:

```bash
python -m venv env_gradio
.\env_gradio\Scripts\activate  # En Windows
```

3. Instalá las dependencias:

```bash
pip install -r requirements.txt
```

4. Creá un archivo `.env` con tu clave de API de Google:

```dotenv
GOOGLE_API_KEY=tu_clave_secreta
```

## 💻 Modo consola
Para correr el asistente desde la terminal:

```bash
python main.py
```

- Desde ahí se puede hacer preguntas directamente y ver de qué documentos se extrajo la respuesta (solo en consola).

## 🌐 Modo interfaz web
Para lanzar el asistente con interfaz gráfica:

```bash
python app_gradio.py
```

- Se abrirá una interfaz en tu navegador.

Podés hacerle preguntas de ejemplo o personalizadas.

---

## 🖼️ Vista previa
[Screenshot Asistente Virtual](https://github.com/alvarezayelen11/chatbot_gradio/blob/master/screenshot_gradio.png)

---

## 🧑‍💻 Autor
- [@alvarezayelen11](https://github.com/alvarezayelen11)

---

## 📢 Feedback
If you have any comments, please write to me.
