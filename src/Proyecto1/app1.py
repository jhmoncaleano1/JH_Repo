import streamlit as st

st.title("Generador de Presupuesto")

proyecto = st.text_input("Nombre del proyecto")
horas_estimadas = st.number_input("Horas estimadas", min_value=0.0)
valor_hora = st.number_input("Valor por hora", min_value=0.0)
tiempo_estimado = st.text_input("Tiempo estimado (ej. 3 semanas)")

if st.button("Calcular presupuesto"):
    costo_total = horas_estimadas * valor_hora
    st.success(f"Costo total estimado: ${costo_total:,.0f} COP")

    # Puede luego guardar, generar PNG o PDF con los datos.
