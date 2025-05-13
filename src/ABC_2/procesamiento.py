import pandas as pd
import os

def detectar_archivo_excel(carpeta="data"):
    for archivo in os.listdir(carpeta):
        if archivo.endswith(".xlsx"):
            return os.path.join(carpeta, archivo)
    raise FileNotFoundError("No se encontró ningún archivo .xlsx en la carpeta 'data'.")

def cargar_datos():
    archivo = detectar_archivo_excel()
    df = pd.read_excel(archivo)
    return df
