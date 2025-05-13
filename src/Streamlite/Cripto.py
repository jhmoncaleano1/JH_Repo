# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Datos iniciales de precios y porcentajes
data = {
    "Criptomoneda": [
        "Bitcoin (BTC)", "Ethereum (ETH)", "Solana (SOL)", "Chainlink (LINK)",
        "Polygon (MATIC)", "Stablecoins", "XRT (Robonomics)", 
        "Avalanche (AVAX)", "Arbitrum (ARB)", "Aptos/SUI", "Token especulativo"
    ],
    "Precio Inicial": [65000, 3200, 140, 15, 1, 1, 3.5, 38, 1.1, 9, 2],
    "% Moderado": [38, 28, 10, 8, 5, 8, 3, 0, 0, 0, 0],
    "% Agresivo": [0, 22, 18, 10, 0, 5, 5, 10, 10, 10, 10],
}

df = pd.DataFrame(data)

df["Precio Actual"] = [
    st.number_input(f"Precio actual de {row['Criptomoneda']}", value=row["Precio Inicial"]) 
    for _, row in df.iterrows()
]

# Función para calcular rendimiento
def calcular_rendimiento(precio_inicial, precio_actual):
    return (precio_actual - precio_inicial) / precio_inicial * 100

df["Rendimiento %"] = df.apply(
    lambda row: calcular_rendimiento(row["Precio Inicial"], row["Precio Actual"]), axis=1
)

# Mostrar tablas y gráficos
st.title("📊 Dashboard Cripto: Perfiles Moderado y Agresivo")

st.subheader("📈 Rendimiento de Criptomonedas")
st.dataframe(df[["Criptomoneda", "Precio Inicial", "Precio Actual", "Rendimiento %"]])

st.subheader("📉 Cambios superiores al ±20%")
alertas = df[np.abs(df["Rendimiento %"]) > 20]
st.warning(alertas[["Criptomoneda", "Rendimiento %"]])

# Gráficos de portafolios
st.subheader("🧩 Portafolio Moderado")
df_moderado = df[df["% Moderado"] > 0]
fig_moderado = px.pie(df_moderado, values="% Moderado", names="Criptomoneda", title="Distribución Moderado")
st.plotly_chart(fig_moderado)

st.subheader("🔥 Portafolio Agresivo")
df_agresivo = df[df["% Agresivo"] > 0]
fig_agresivo = px.pie(df_agresivo, values="% Agresivo", names="Criptomoneda", title="Distribución Agresivo")
st.plotly_chart(fig_agresivo)

st.caption("Prototipo generado por IA – actualizado con XRT y monitoreo de rendimiento.")
