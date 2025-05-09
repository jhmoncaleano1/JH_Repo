import pandas as pd
from sklearn.linear_model import LinearRegression

# Datos históricos
data = {
    "dia": [1, 2, 3, 4, 5, 6, 7],
    "ventas": [100, 120, 130, 150, 170, 180, 200]
}
df = pd.DataFrame(data)

# Entrenar modelo
X = df[["dia"]]
y = df["ventas"]
modelo = LinearRegression()
modelo.fit(X, y)

# Pedir entrada del usuario
try:
    dia_a_predecir = int(input("Ingrese el número de día a predecir (ej: 8): "))
    prediccion = modelo.predict([[dia_a_predecir]])
    print(f"🔮 Predicción de ventas para el día {dia_a_predecir}: {prediccion[0]:.2f} unidades")
except ValueError:
    print("❌ Error: Debe ingresar un número entero.")
