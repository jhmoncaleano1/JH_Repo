# factura.py
from datetime import datetime

class Factura:
    def __init__(self, cliente):
        self.cliente = cliente
        self.productos = []
        self.fecha = datetime.now()

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def calcular_total(self):
        return sum(p.precio for p in self.productos)

    def mostrar_factura(self):
        productos_str = "\n".join(str(p) for p in self.productos)
        total = self.calcular_total()
        return (f"Factura para {self.cliente.nombre} ({self.fecha.strftime('%Y-%m-%d')})\n"
                f"Productos:\n{productos_str}\n"
                f"Total: ${total:.2f}")