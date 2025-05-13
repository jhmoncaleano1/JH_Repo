# src/main.py

from archivos.procesador_excel import leer_archivo_excel

ruta = "data/Inv_Fc_Cli.xlsx"
datos = leer_archivo_excel(ruta)

for nombre_hoja, df in datos.items():
    print(f"📊 {nombre_hoja}: {df.shape[0]} filas, {df.shape[1]} columnas")

