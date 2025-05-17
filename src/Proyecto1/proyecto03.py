from PIL import Image, ImageDraw, ImageFont
import datetime

def generar_presupuesto_png(cliente, productos, nombre_archivo="presupuesto_final_7.png"):
    ancho = 794
    alto_base = 300 + len(productos) * 40 + 100
    imagen = Image.new("RGB", (ancho, alto_base), "white")
    draw = ImageDraw.Draw(imagen)

    try:
        fuente_titulo = ImageFont.truetype("arial.ttf", 24)
        fuente = ImageFont.truetype("arial.ttf", 20)
    except:
        fuente_titulo = ImageFont.load_default()
        fuente = ImageFont.load_default()

    draw.rectangle((30, 30, 130, 130), fill="gray")
    draw.text((50, 80), "EASI", fill="white", font=fuente)

    draw.text((150, 40), "PRESUPUESTO COMERCIAL", font=fuente_titulo, fill="black")
    draw.line((30, 150, ancho - 30, 150), fill="black", width=2)

    draw.text((30, 160), f"Cliente: {cliente}", font=fuente, fill="black")
    draw.text((30, 190), f"Fecha: {datetime.date.today()}", font=fuente, fill="black")

    y = 240
    draw.line((30, y - 10, ancho - 30, y - 10), fill="black", width=1)
    draw.text((30, y), "Producto", font=fuente, fill="black")
    draw.text((350, y), "Cantidad", font=fuente, fill="black")
    draw.text((500, y), "Precio", font=fuente, fill="black")
    draw.text((650, y), "Subtotal", font=fuente, fill="black")
    y += 30

    total = 0
    for nombre, cantidad, precio in productos:
        subtotal = cantidad * precio
        draw.text((30, y), nombre, font=fuente, fill="black")
        draw.text((350, y), str(cantidad), font=fuente, fill="black")
        draw.text((500, y), f"${precio:,.0f}", font=fuente, fill="black")
        draw.text((650, y), f"${subtotal:,.0f}", font=fuente, fill="black")
        y += 30
        total += subtotal

    y += 10
    draw.line((30, y, ancho - 30, y), fill="black", width=1)
    y += 20
    draw.text((500, y), "TOTAL:", font=fuente, fill="black")
    draw.text((650, y), f"${total:,.0f}", font=fuente, fill="black")

    imagen = imagen.crop((0, 0, ancho, y + 80))  # ✂️ Recorte preciso al contenido
    imagen.save(nombre_archivo)
    print(f"✅ Presupuesto de_generado : {nombre_archivo}")

# Ejemplo
productos = [
    ("Monitor 24\"", 2, 620000),
    ("Teclado inalámbrico", 1, 180000),
    ("Mouse óptico", 2, 45000)
]

generar_presupuesto_png(
    cliente="Distribuidora Siglo XV",
    productos=productos
)

