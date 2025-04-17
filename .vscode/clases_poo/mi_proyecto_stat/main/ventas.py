# ========== main/ventas.py ==========
import pandas as pd
from app.estadisticas import calcular_total_ventas, ventas_por_cliente
from app.graficos import grafico_barras_clientes, grafico_lineas_fecha

def leer_excel(ruta):
    return pd.read_excel(ruta, engine='openpyxl', parse_dates=['Fecha'])

if __name__ == "__main__":
    ruta = r"C:\\Users\\PC\\Documents\\mi_proyecto_python\\.vscode\\mi_proyecto_stat\\data\\ventas.xlsx"
    df = leer_excel(ruta)

    print("Total de ventas:", calcular_total_ventas(df))
    print("Ventas por cliente:\n", ventas_por_cliente(df))

    grafico_barras_clientes(df)
    grafico_lineas_fecha(df)