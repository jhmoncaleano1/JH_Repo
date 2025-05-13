from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generar_pdf(dataframe, archivo="reporte.pdf"):
    c = canvas.Canvas(archivo, pagesize=letter)
    c.drawString(100, 750, "Reporte de Ventas")

    y = 700
    for index, row in dataframe.iterrows():
        texto = f"Cliente: {row['cliente']}, Ventas: {row['ventas']}"
        c.drawString(100, y, texto)
        y -= 20

    c.save()
    print(f"PDF generado: {archivo}")
