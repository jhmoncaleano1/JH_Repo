from procesamiento import cargar_datos
from reportes import generar_pdf, generar_grafico

def main():
    print("Cargando datos desde archivo Excel...")
    df = cargar_datos()
    print(df)

    print("Generando gráfico de ventas...")
    generar_grafico(df)

    print("Generando PDF con gráfico...")
    generar_pdf(df)

if __name__ == "__main__":
    main()
