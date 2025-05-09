import shap
import streamlit as st
import xgboost
import pandas as pd

# Modelo entrenado
model = xgboost.XGBClassifier()
# ... ya entrenado con datos ...

# Cargar datos nuevos
data = pd.read_csv("cliente_nuevo.csv")

# Predicción
pred = model.predict(data)

# Explicación SHAP
explainer = shap.Explainer(model)
shap_values = explainer(data)

# Mostrar en Streamlit
st.write("Predicción del modelo:", pred)
st.write("Explicación de la predicción:")
st_shap(shap.plots.waterfall(shap_values[0]), height=300)
