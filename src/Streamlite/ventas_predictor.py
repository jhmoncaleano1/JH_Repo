import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# Título del dashboard
st.title("📈 Predicción de Ventas con Machine Learning")

# Datos de ejemplo
data = {
    "dia": [1, 2, 3, 4, 5, 6, 7],
    "ventas": [100, 120, 130, 150, 170, 180, 200]
}
df = pd.DataFrame(data)

# Mostrar tabla
st.subheader("📊 Datos históricos")
st.dataframe(df)

# Entrenar modelo
X = df[["dia"]]
y = df["ventas"]
modelo = LinearRegression()
modelo.fit(X, y)

# Selector de día a predecir
st.subheader("🔮 Ingrese el día a predecir")
dia_a_predecir = st.slider("Seleccione un día (entero)", min_value=1, max_value=30, value=8)

# Realizar predicción
prediccion = modelo.predict([[dia_a_predecir]])

# Mostrar resultado
st.success(f"🔍 Predicción de ventas para el día {dia_a_predecir}: {prediccion[0]:.2f} unidades")

# Gráfico comparativo
df_pred = pd.DataFrame({
    "dia": list(df["dia"]) + [dia_a_predecir],
    "ventas": list(df["ventas"]) + [prediccion[0]]
})
st.subheader("📉 Evolución de ventas (incluyendo predicción)")
st.line_chart(df_pred.set_index("dia"))
