import pandas as pd
from procesamiento import cargar_datos
from reportes import generar_pdf

def main():
    df = cargar_datos()
    if df is None or df.empty:
        print("⚠️ No se pudo cargar el DataFrame.")
        return

    print("✅ Datos cargados:\n", df)
    generar_pdf(df)
    print("📄 PDF generado con éxito.")

if __name__ == "__main__":
    main()


