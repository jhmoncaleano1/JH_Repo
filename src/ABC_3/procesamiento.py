import pandas as pd
import os

def detectar_archivo_excel(carpeta="data"):
    archivos = sorted(
        [f for f in os.listdir(carpeta) if f.endswith(".xlsx")],
        key=lambda x: os.path.getmtime(os.path.join(carpeta, x)),
        reverse=True
    )
    if archivos:
        return os.path.join(carpeta, archivos[0])
    else:
        raise FileNotFoundError("No se encontró ningún archivo .xlsx en la carpeta 'data'.")

def cargar_datos():
    archivo = detectar_archivo_excel()
    df = pd.read_excel(archivo)
    return df

def guardar_snapshot(df, path="ultimo_snapshot.csv"):
    df.to_csv(path, index=False)

def cargar_snapshot_anterior(path="ultimo_snapshot.csv"):
    if os.path.exists(path):
        return pd.read_csv(path)
    return None
