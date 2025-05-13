import pandas as pd

def cargar_datos():
    # Simulación de carga de datos
    data = {
        'cliente': ['Alice', 'Bob', 'Carlos'],
        'ventas': [150, 200, 300]
    }
    df = pd.DataFrame(data)
    return df

    