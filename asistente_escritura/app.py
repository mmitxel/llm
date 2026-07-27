import google.generativeai as genai
import streamlit as st

# Configuración básica de la página
st.set_page_config(page_title="Tutor de Mandarín", page_icon="🐉", layout="centered")

st.title("🐉 Tutor Virtual de Mandarín")
st.write(
    "¡Hola! Soy tu laoshi (profesor) virtual. Puedo ayudarte a desglosar caracteres, entender su gramática y practicar su pronunciación."
)

# Configurar API Key
# Intentar leer la API key de los secretos de Streamlit
if "GEMINI_API_KEY" in st.secrets:
    api_key = st.secrets["GEMINI_API_KEY"]

else:
    # Si no existe el archivo, pedirla por la interfaz
    api_key = st.text_input(
        "Ingresa tu Google Gemini API Key para empezar:", type="password"
    )

if api_key:
    genai.configure(api_key=api_key)

    # Seleccionar la tarea educativa
    tarea = st.selectbox(
        "¿Qué deseas estudiar hoy?",
        (
            "Analizar un carácter/palabra",
            "Generar ejemplos en contexto",
            "Diferencias entre palabras similares",
        ),
    )

    if tarea == "Analizar un carácter/palabra":
        texto_usuario = st.text_input(
            "Ingresa el carácter o palabra en chino (ej. 汉字, 明):"
        )
        if st.button("Analizar"):
            if texto_usuario:
                with st.spinner("Desglosando el carácter..."):
                    try:
                        model = genai.GenerativeModel(st.secrets["GEMINI_MODEL"])
                        prompt = f"""
                        Actúa como un profesor experto de chino mandarín. Analiza el siguiente texto: '{texto_usuario}'.
                        Proporciona la siguiente estructura exacta:
                        1. **Pinyin**: (con marcas tonales)
                        2. **Significado Principal**: 
                        3. **Desglose de Radicales/Raíces**: (Explica los componentes del carácter para ayudar a memorizarlo)
                        4. **Nivel aproximado HSK**: 
                        """
                        response = model.generate_content(prompt)
                        st.subheader("Análisis:")
                        st.write(response.text)
                    except Exception as e:
                        st.error(f"Error: {e}")
            else:
                st.warning("Por favor, ingresa un carácter.")

    elif tarea == "Generar ejemplos en contexto":
        texto_usuario = st.text_input(
            "Ingresa la palabra o regla gramatical que quieres practicar:"
        )
        if st.button("Crear ejemplos"):
            if texto_usuario:
                with st.spinner("Creando oraciones..."):
                    try:
                        model = genai.GenerativeModel(st.secrets["GEMINI_MODEL"])
                        prompt = f"""
                        Escribe 3 oraciones de ejemplo usando la palabra o concepto '{texto_usuario}' en chino mandarín.
                        Para cada oración incluye:
                        - Los caracteres chinos.
                        - El pinyin.
                        - La traducción al español.
                        Ve de la oración más sencilla a la más compleja.
                        """
                        response = model.generate_content(prompt)
                        st.subheader("Ejemplos:")
                        st.write(response.text)
                    except Exception as e:
                        st.error(f"Error: {e}")
            else:
                st.warning("Por favor, ingresa una palabra.")

    elif tarea == "Diferencias entre palabras similares":
        palabra1 = st.text_input("Palabra 1 (ej. 认为):")
        palabra2 = st.text_input("Palabra 2 (ej. 以为):")
        if st.button("Comparar"):
            if palabra1 and palabra2:
                with st.spinner("Analizando matices..."):
                    try:
                        model = genai.GenerativeModel(st.secrets["GEMINI_MODEL"])
                        prompt = f"""
                        Explica la diferencia de uso y contexto entre '{palabra1}' y '{palabra2}' en chino mandarín.
                        Da una explicación clara y proporciona un ejemplo corto para cada una donde NO sean intercambiables.
                        """
                        response = model.generate_content(prompt)
                        st.subheader("Comparación:")
                        st.write(response.text)
                    except Exception as e:
                        st.error(f"Error: {e}")
            else:
                st.warning("Por favor, ingresa ambas palabras.")
else:
    st.info("Para usar el tutor, necesitas tu API Key de Google Gemini.")
