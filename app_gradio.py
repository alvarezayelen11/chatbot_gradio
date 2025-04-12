# Importamos las librerías
import gradio as gr
from main import generar_respuesta, inicializar_vectorstore

# Cargamos el vectorstore una sola vez
vectorstore = inicializar_vectorstore()

def responder_gradio(pregunta):
    if pregunta.lower() in ["salir", "exit", "quit"]:
        return "Gracias por visitar el asistente de Juan Pérez. ¡Hasta la próxima!"
    
    respuesta, _ = generar_respuesta(pregunta, vectorstore)  # Ignoramos la fuente
    return respuesta

# Interfaz 
iface = gr.Interface(
    fn=responder_gradio,
    inputs=gr.Textbox(
        lines=2,
        placeholder="Escribí tu pregunta aquí...",
        label="Tu pregunta"
    ),
    outputs=gr.Textbox(label="Respuesta", lines=5),  # Solo un output
    title="🤖 Asistente Virtual de Juan Pérez",
    description="Puedes preguntarle sobre su experiencia laboral, formación y habilidades. El asistente estará encantado de ayudarte.",
    theme="soft",
    allow_flagging="never",
    examples=[
        "¿Juan tiene experiencia con SQL?",
        "¿Dónde estudió Juan?",
        "What languages does Juan speak?",
        "¿Cuáles son sus fortalezas y debilidades?"
    ],
    article="🌐 Más sobre mí: [LinkedIn de Ayelén Álvarez](https://www.linkedin.com/in/-ayelen-alvarez/)"
)

if __name__ == "__main__":
    iface.launch(share=False)  # Cambiar a True para un perfil público