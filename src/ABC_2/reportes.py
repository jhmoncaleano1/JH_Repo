from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import matplotlib.pyplot as plt

def generar_grafico(df, imagen="grafico.png"):
    plt.figure(figsize=(6, 4))
    plt.bar(df["cliente"], df["ventas"], color="skyblue")
    plt.title("Ventas por Cliente")
    plt.xlabel("Cliente")
    plt.ylabel("Ventas")
    plt.tight_layout()
    plt.savefig(imagen)
    plt.close()
    print(f"Gráfico guardado como {imagen}")

def generar_pdf(df, archivo="reporte.pdf", imagen="grafico.png"):
    c = canvas.Canvas(archivo, pagesize=letter)
    c.drawString(100, 750, "Reporte de Ventas")

    y = 700
    for index, row in df.iterrows():
        texto = f"Cliente: {row['cliente']}, Ventas: {row['ventas']}"
        c.drawString(100, y, texto)
        y -= 20

    # Insertar gráfico
    c.drawImage(imagen, 100, y - 250, width=400, height=300)
    c.save()
    print(f"PDF generado: {archivo}")
