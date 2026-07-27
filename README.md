
# 🐉 Tutor Virtual de Mandarín

Este es un proyecto de un Tutor Virtual impulsado por Inteligencia Artificial utilizando **Streamlit** para la interfaz gráfica y **Google Gemini API** (modelo 1.5 Flash) como motor de lenguaje. Está diseñado específicamente para asistir en el aprendizaje del idioma chino mandarín, desglosando caracteres, explicando gramática y generando ejemplos contextuales.

## 🚀 Funcionalidades

El tutor cuenta con tres funciones principales diseñadas para facilitar el estudio del idioma:

1. **Analizar un carácter o palabra**: Ingresa cualquier Hanzi (ej. 汉字) y la IA desglosará su Pinyin (con marcas tonales), significado principal, componentes/radicales etimológicos para facilitar su memorización, y su nivel aproximado del HSK.
2. **Generar ejemplos en contexto**: Permite ingresar una palabra o regla gramatical para obtener 3 oraciones de ejemplo (de menor a mayor dificultad), incluyendo caracteres, pinyin y su traducción al español.
3. **Diferencias entre palabras similares**: Compara dos términos (ej. 认为 vs 以为) para explicar sus matices, diferencias de uso y ejemplos claros donde no son intercambiables.

## 🛠 Requisitos Previos

Para utilizar esta aplicación necesitas:

- Python 3.8 o superior instalado en tu sistema.
- Una **API Key de Google Gemini** (Puedes obtenerla gratuitamente en [Google AI Studio](https://aistudio.google.com/)).
- Un nombre de **modelo de Google Gemini** válido (Puedes encontrarlos en https://ai.google.dev/gemini-api/docs/models)

## 📦 Instalación y Configuración

1. Navega hasta la carpeta del proyecto en tu terminal:
   ```bash
   cd LLM/asistente_escritura
   ```

2. (Recomendado) Crea un entorno virtual en la raíz de tu repositorio para instalar las dependencias sin afectar tu sistema:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # En Mac/Linux
   # .venv\Scripts\activate   # En Windows
   ```

3. Instala las dependencias requeridas:
   ```bash
   pip install streamlit google-generativeai
   ```

4. **Configura tus secretos (API Key y Modelo):**
Crea una carpeta oculta llamada `.streamlit` dentro del directorio del proyecto y un archivo `secrets.toml` dentro de ella:
   ```bash
   mkdir .streamlit
   touch .streamlit/secrets.toml
   ```

5. Abre el archivo `secrets.toml` y agrega tus credenciales y la configuración del modelo de forma segura:
   ```toml
   GEMINI_API_KEY = "TU_API_KEY_AQUI"
   GEMINI_MODEL = "GEMINI_MODEL"
   ```

## ▶️ Uso

Para iniciar la aplicación, asegúrate de tener tu entorno virtual activado, estar posicionado en la carpeta `asistente_escritura` y ejecuta el siguiente comando:

   ```bash
   streamlit run app.py
   ```

* La aplicación se abrirá automáticamente en tu navegador web predeterminado (usualmente en `http://localhost:8501`).
* Si configuraste correctamente tu archivo `secrets.toml`, el tutor detectará tu clave y modelo automáticamente. En caso de que falte el archivo, la interfaz te pedirá ingresar tu API Key temporalmente para esa sesión.

## 📚 Tecnologías Utilizadas

* [Python](https://www.python.org/)
* [Streamlit](https://streamlit.io/) (Interfaz de usuario web)
* [Google Generative AI](https://ai.google.dev/) (Modelo Gemini 3.5 Flash optimizado para baja latencia)