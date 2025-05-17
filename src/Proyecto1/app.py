import streamlit as st
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont

# Título de la app
#Se ejecuta con "streamlit run app.py"
st.title("📋 Generador de Presupuesto Comercial")

# Captura de datos
proyecto = st.text_input("Digite el nombre del proyecto:")
cliente = st.text_input("Nombre del cliente:")
fecha = st.date_input("Fecha del presupuesto:", value=datetime.today())
horas_estimadas = st.number_input("Horas estimadas", min_value=0)
valor_hora = st.number_input("Valor por hora", min_value=0)
tiempo_estimado = st.text_input("Tiempo estimado (ej: 2 semanas)")

# Calcular presupuesto
if proyecto and cliente and horas_estimadas > 0 and valor_hora > 0:
    costo_total = horas_estimadas * valor_hora

    st.subheader("🧾 Resumen del Presupuesto")
    st.markdown(f"""
    **Proyecto:** {proyecto}  
    **Cliente:** {cliente}  
    **Fecha:** {fecha.strftime('%Y-%m-%d')}  
    **Horas estimadas:** {horas_estimadas}  
    **Valor por hora:** ${valor_hora:,.0f}  
    **Tiempo estimado:** {tiempo_estimado}  
    **Total estimado:** ${costo_total:,.0f}
    """)

    # Botón para generar imagen
    if st.button("📸 Generar imagen PNG del presupuesto"):
        img = Image.new("RGB", (700, 400), color="white")
        draw = ImageDraw.Draw(img)
        font_title = ImageFont.truetype("arial.ttf", 24)
        font_text = ImageFont.truetype("arial.ttf", 16)

        draw.text((20, 20), "PRESUPUESTO COMERCIAL", fill="black", font=font_title)
        draw.text((20, 70), f"Proyecto: {proyecto}", fill="black", font=font_text)
        draw.text((20, 100), f"Cliente: {cliente}", fill="black", font=font_text)
        draw.text((20, 130), f"Fecha: {fecha.strftime('%Y-%m-%d')}", fill="black", font=font_text)
        draw.text((20, 160), f"Horas estimadas: {horas_estimadas}", fill="black", font=font_text)
        draw.text((20, 190), f"Valor por hora: ${valor_hora:,.0f}", fill="black", font=font_text)
        draw.text((20, 220), f"Tiempo estimado: {tiempo_estimado}", fill="black", font=font_text)
        draw.text((20, 260), f"TOTAL: ${costo_total:,.0f}", fill="black", font=font_title)

        output_path = "presupuesto_generado.png"
        img.save(output_path)

        st.success("Imagen generada con éxito 🎉")
        st.image(output_path, caption="Presupuesto generado")

else:
    st.warning("Por favor, complete todos los campos para generar el presupuesto.")
