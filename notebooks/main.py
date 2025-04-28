import os
import pandas as pd
import matplotlib.pyplot as plt

# Ruta absoluta basada en la ubicación actual del script
ruta_archivo = os.path.join(os.path.dirname(__file__), 'data', 'dato3.csv')

# Leer el archivo CSV
try:
    df = pd.read_csv(ruta_archivo)
    print("Archivo cargado correctamente.")
except FileNotFoundError:
    print("❌ No se encontró el archivo CSV. Verifique que 'dato3.csv' esté en la carpeta 'data'.")
    exit()

# Mostrar los primeros datos
print(df.head())

# Aquí puede agregar sus gráficos o procesamiento
# Ejemplo de gráfico básico si hay columnas 'Nombre' y 'Salario'
if "Nombre" in df.columns and "Salario" in df.columns:
    plt.figure(figsize=(8,5))
    plt.bar(df["Nombre"], df["Salario"], color="skyblue")
    plt.title("Salarios por Nombre")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
else:
    print("⚠️ Las columnas 'Nombre' y 'Salario' no están disponibles en el archivo.")
