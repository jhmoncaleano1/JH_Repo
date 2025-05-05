# prototipo_ia_streamlit.py

import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Título del dashboard
st.title("Prototipo IA - Análisis de Datos y Visualización")

# Subir archivo Excel
archivo = st.file_uploader("Suba un archivo .xlsx con datos", type=["xlsx"])

if archivo:
    hojas = pd.ExcelFile(archivo).sheet_names
    hoja = st.selectbox("Seleccione la hoja a analizar", hojas)

    df = pd.read_excel(archivo, sheet_name=hoja)
    st.subheader("Vista previa de los datos")
    st.dataframe(df.head())

    columnas_numericas = df.select_dtypes(include='number').columns.tolist()

    # Simple IA: regresión lineal entre dos variables
    st.subheader("Modelo de Regresión Lineal")
    x_col = st.selectbox("Variable Independiente (X)", columnas_numericas)
    y_col = st.selectbox("Variable Dependiente (Y)", columnas_numericas, index=1 if len(columnas_numericas) > 1 else 0)

    if x_col != y_col:
        X = df[[x_col]]
        y = df[y_col]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        modelo = LinearRegression()
        modelo.fit(X_train, y_train)

        y_pred = modelo.predict(X_test)
        resultado_df = pd.DataFrame({"X_test": X_test[x_col], "y_real": y_test, "y_pred": y_pred})

        st.success(f"Coeficiente: {modelo.coef_[0]:.4f}, Intercepto: {modelo.intercept_:.4f}")

        fig = px.scatter(resultado_df, x="X_test", y="y_real", title="Predicciones vs Valores Reales")
        fig.add_scatter(x=resultado_df["X_test"], y=resultado_df["y_pred"], mode='lines', name='Predicciones')
        st.plotly_chart(fig)
    else:
        st.warning("Las variables X y Y deben ser diferentes.")
