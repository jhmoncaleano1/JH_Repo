# Ejemplo de uso de la API de Gemini en Python
# Primero necesitas instalar la biblioteca: pip install google-generativeai

import google.generativeai as genai
import os
from IPython.display import Markdown, display

# Configura tu clave API
# En un entorno real, deberías guardar esto en variables de entorno
API_KEY = "AIzaSyAwzCRF1-SgP_yWuNJMcrnGrTZtZd9IRCcAIzaSy"  # Reemplaza con tu clave API real
genai.configure(api_key=API_KEY)

# Función para mostrar respuestas de texto
def display_response(response):
    print("\nRespuesta de Gemini:\n")
    print(response.text)
    print("\n" + "-"*50 + "\n")

# 1. Ejemplo básico - Generación de texto
def ejemplo_generacion_texto():
    print("Ejemplo 1: Generación básica de texto")
    
    # Inicializa el modelo
    model = genai.GenerativeModel('gemini-pro')
    
    # Envía una solicitud al modelo
    response = model.generate_content("Explica las APIs REST en 3 párrafos sencillos")
    
    # Muestra la respuesta
    display_response(response)

# 2. Ejemplo - Análisis con parámetros de configuración
def ejemplo_con_parametros():
    print("Ejemplo 2: Generación con parámetros")
    
    model = genai.GenerativeModel('gemini-pro')
    
    # Configuración para controlar la respuesta
    generation_config = {
        "temperature": 0.9,  # Más creativo (0.0 a 1.0)
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 200,  # Limita la longitud de la respuesta
    }
    
    prompt = "Dame 5 ideas creativas para un proyecto de programación para principiantes"
    
    response = model.generate_content(
        prompt,
        generation_config=generation_config
    )
    
    display_response(response)

# 3. Ejemplo - Chat con contexto
def ejemplo_chat():
    print("Ejemplo 3: Conversación con contexto")
    
    model = genai.GenerativeModel('gemini-pro')
    chat = model.start_chat(history=[])
    
    # Primera interacción
    response = chat.send_message("¿Qué es Python?")
    print("Pregunta 1: ¿Qué es Python?")
    display_response(response)
    
    # Segunda interacción (mantiene el contexto)
    response = chat.send_message("¿Cuáles son sus principales características?")
    print("Pregunta 2: ¿Cuáles son sus principales características?")
    display_response(response)
    
    # Tercera interacción
    response = chat.send_message("Dame un ejemplo de código sencillo")
    print("Pregunta 3: Dame un ejemplo de código sencillo")
    display_response(response)

# 4. Ejemplo - Análisis multimodal (texto + imagen)
def ejemplo_multimodal():
    print("Ejemplo 4: Análisis multimodal (requiere gemini-pro-vision)")
    
    # Para este ejemplo necesitarías una imagen
    try:
        from PIL import Image
        
        # Cambia esta ruta a una imagen real en tu sistema
        imagen_path = "ruta/a/tu/imagen.jpg"
        imagen = Image.open(imagen_path)
        
        model = genai.GenerativeModel('gemini-pro-vision')
        
        response = model.generate_content([
            "Describe detalladamente lo que ves en esta imagen",
            imagen
        ])
        
        display_response(response)
    except Exception as e:
        print(f"No se pudo ejecutar el ejemplo multimodal: {e}")
        print("Para usar esta funcionalidad, necesitas tener una imagen y la biblioteca PIL instalada.")
        print("Además, debes tener acceso al modelo gemini-pro-vision")

# Ejecutar los ejemplos
def main():
    print("DEMOSTRACION DE LA API DE GEMINI\n")
    print("=" * 50)
    
    # Ejecuta los ejemplos uno por uno
    ejemplo_generacion_texto()
    ejemplo_con_parametros()
    ejemplo_chat()
    # ejemplo_multimodal()  # Descomentar si tienes una imagen para probar

if __name__ == "__main__":
    main()