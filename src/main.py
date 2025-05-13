import os
from modelo_ventas import SistemaVentas



# Imprimir factura
# Datos del cliente y productos
cliente = "Juan Pérez"
productos = [
    {"nombre": "Producto 1", "precio": 100},
    {"nombre": "Producto 2", "precio": 150}
]

# Crear una instancia de la clase SistemaVentas
sistema = SistemaVentas(cliente, productos)

# Imprimir la factura
print(sistema.generar_factura())