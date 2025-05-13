import pandas as pd
from datetime import datetime


# modelo_ventas.py

class SistemaVentas:
    def __init__(self, cliente, productos):
        """Constructor que recibe el cliente y los productos."""
        self.cliente = cliente
        self.productos = productos

    def calcular_total(self):
        """Método para calcular el total de la factura."""
        total = sum(producto['precio'] for producto in self.productos)
        return total

    def generar_factura(self):
        """Generar una factura simple con los datos de cliente y total."""
        factura = f"Factura para {self.cliente}\n"
        factura += f"Total a pagar: ${self.calcular_total()}"
        return factura


class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre

class Producto:
    def __init__(self, id_producto, nombre, precio):
        self.id = id_producto
        self.nombre = nombre
        self.precio = precio

class Factura:
    def __init__(self, cliente):
        self.cliente = cliente
        self.items = []
        self.fecha = datetime.now()

    def agregar_producto(self, producto, cantidad):
        self.items.append((producto, cantidad))

    def calcular_total(self):
        return sum(p.precio * c for p, c in self.items)

    def exportar_txt(self, ruta):
        with open(ruta, 'w', encoding='utf-8') as f:
            f.write(f"Factura para: {self.cliente.nombre}\n")
            f.write(f"Fecha: {self.fecha.strftime('%Y-%m-%d %H:%M')}\n\n")
            f.write("Productos:\n")
            for p, c in self.items:
                f.write(f"- {p.nombre} x{c}: ${p.precio * c:,.2f}\n")
            f.write(f"\nTotal: ${self.calcular_total():,.2f}")
print("termine")
