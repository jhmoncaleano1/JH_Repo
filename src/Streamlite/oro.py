import streamlit as st
import pandas as pd
import datetime

st.set_page_config(page_title="Dashboard de Oro", layout="wide")

# --- Sidebar ---
st.sidebar.title("Parámetros de Simulación")

# Entradas del usuario
precio_actual = st.sidebar.number_input("Precio actual por gramo (COP)", value=465901)
precio_1g = st.sidebar.number_input("Precio lingote 1g (COP)", value=630000)
precio_5g = st.sidebar.number_input("Precio lingote 5g (COP)", value=3100000)
precio_onza = st.sidebar.number_input("Precio lingote 1 onza (COP)", value=18500000)

cantidad_gramos = st.sidebar.slider("Cantidad de gramos que desea comprar", 1, 100, 10)

# Proyección a 3 años
anio_actual = datetime.datetime.now().year
proyeccion = {
    anio_actual: precio_actual,
    anio_actual + 1: round(precio_actual * 1.08),
    anio_actual + 2: round(precio_actual * 1.15),
    anio_actual + 3: round(precio_actual * 1.25)
}

# --- Layout Principal ---
st.title("💰 Dashboard Interactivo del Oro 24K")
st.markdown("""
Este dashboard le permite simular compras de oro en Bogotá y visualizar proyecciones para los próximos tres años.
""")

# --- Sección de Proveedores ---
st.subheader("📍 Proveedores Recomendados en Bogotá")
proveedores = pd.DataFrame([
    ["Oroexpress", "1g, 5g, 1 onza", "https://oroexpress.com.co", "630,000 / 3,100,000 / 18,500,000"],
    ["Alloy", "Gramos 24K certificados", "https://alloy.com.co", "478,890 / gramo"],
    ["Triángulo de Oro", "Joyas personalizadas, compra de oro", "https://triangulodeoro.com.co", "397,906 / gramo"],
    ["Orosilver", "Joyas y compra de metales", "https://orosilver.com.co", "Precios variables"]
], columns=["Proveedor", "Productos", "Sitio Web", "Precios Aproximados"])

st.dataframe(proveedores, use_container_width=True)

# --- Cálculo de inversión ---
st.subheader("💸 Simulación de Compra")
total = cantidad_gramos * precio_actual
st.markdown(f"**Total estimado para {cantidad_gramos} gramos:** ${total:,.0f} COP")

# --- Gráfico de proyección ---
st.subheader("📊 Proyección del Precio del Oro (COP por gramo)")
df_proj = pd.DataFrame({
    "Año": list(proyeccion.keys()),
    "Precio proyectado": list(proyeccion.values())
})
st.line_chart(df_proj.set_index("Año"))

# Footer
st.markdown("---")
st.caption("Datos actualizados al 7 de mayo de 2025. Precios sujetos a cambios.")
