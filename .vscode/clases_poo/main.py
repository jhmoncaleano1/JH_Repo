# main.py
from cliente import Cliente
from producto import Producto
from factura import Factura

# Crear un cliente
cliente1 = Cliente("Juan Pérez", "juan@example.com")

# Crear algunos productos
producto1 = Producto("Laptop", 3500.00)
producto2 = Producto("Mouse", 150.00)

# Crear factura
factura = Factura(cliente1)
factura.agregar_producto(producto1)
factura.agregar_producto(producto2)

# Mostrar la factura
print(factura.mostrar_factura())
