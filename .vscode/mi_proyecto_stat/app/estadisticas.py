# app/estadisticas.py
def calcular_total_ventas(df):
    return df['Monto'].sum()

def ventas_por_cliente(df):
    return df.groupby('Cliente')['Monto'].sum().sort_values(ascending=False)