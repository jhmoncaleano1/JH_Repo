import streamlit as st
import pandas as pd

st.title("Dashboard de ventas")
archivo = st.file_uploader("Suba un archivo Excel")

if archivo:
    df = pd.read_excel(archivo)
    st.write("Vista previa de los datos", df.head())
    st.line_chart(df["ventas"])