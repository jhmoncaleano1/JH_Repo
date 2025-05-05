import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar datos
df = pd.read_excel("Cartera.xlsx")

st.title("Dashboard de Ventas, Cartera y Transporte")

# Filtros
clientes = st.multiselect("Filtrar por cliente:", options=df["Cliente"].unique())
transportadoras = st.multiselect("Filtrar por transportadora:", options=df["Transportadora"].unique())

df_filtered = df.copy()
if clientes:
    df_filtered = df_filtered[df_filtered["Cliente"].isin(clientes)]
if transportadoras:
    df_filtered = df_filtered[df_filtered["Transportadora"].isin(transportadoras)]

# KPIs
st.subheader("Indicadores Clave")
col1, col2, col3 = st.columns(3)
col1.metric("Total Ventas", f"${df_filtered['Valor Total'].sum():,.2f}")
col2.metric("Pedidos Totales", df_filtered['Pedido'].nunique())
col3.metric("Peso Total (kg)", f"{df_filtered['Peso Carga (kg)'].sum():,.2f} kg")

# Gráfico de ventas por cliente
st.subheader("Ventas por Cliente")
ventas_cliente = df_filtered.groupby("Cliente")["Valor Total"].sum().reset_index()
fig1 = px.bar(ventas_cliente, x="Cliente", y="Valor Total", title="Ventas por Cliente")
st.plotly_chart(fig1)

# Gráfico de envíos por transportadora
st.subheader("Actividad por Transportadora")
envios_transportadora = df_filtered["Transportadora"].value_counts().reset_index()
envios_transportadora.columns = ["Transportadora", "Cantidad de envíos"]
fig2 = px.pie(envios_transportadora, names="Transportadora", values="Cantidad de envíos",
              title="Distribución de Envíos por Transportadora")
st.plotly_chart(fig2)

# Cumplimiento de entregas
st.subheader("Análisis de Entregas")
fig3 = px.histogram(df_filtered, x="DiasEntrega", nbins=20, title="Distribución de Días de Entrega")
st.plotly_chart(fig3)