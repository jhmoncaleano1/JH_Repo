import pandas as pd
import os

# Hojas esperadas en el archivo
HOJAS_REQUERIDAS = ["Facturacion", "Clientes", "Cartera", "Inventario"]

def leer_archivo_excel(ruta_archivo):
    if not os.path.exists(ruta_archivo):
        raise FileNotFoundError(f"No se encontró el archivo: {ruta_archivo}")

    print(f"📂 Leyendo archivo: {ruta_archivo}") 
    
    try:
        # Carga todas las hojas
        hojas = pd.read_excel(ruta_archivo, sheet_name=None)
    except Exception as e:
        raise ValueError(f"No se pudo leer el archivo Excel: {e}")
    
    datos = {}
    for hoja in HOJAS_REQUERIDAS:
        if hoja not in hojas:
            raise ValueError(f"Falta la hoja requerida: {hoja}")
        
        df = hojas[hoja].copy()
        df.dropna(how='all', inplace=True)  # Elimina filas completamente vacías
        df.columns = [str(col).strip() for col in df.columns]  # Limpia los nombres de columna
        datos[hoja] = df
        print(f"✅ Hoja '{hoja}' cargada con {len(df)} registros.")

    return datos


