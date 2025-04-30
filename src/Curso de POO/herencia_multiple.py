import datetime
import os
import pandas as pd

def cargar_productos_desde_excel(Curso de POO\productos.xlsx):
    df = pd.read_excel(ruta_excel)
    productos = []
    for _, fila in df.iterrows():
        producto = Producto(codigo=fila["codigo"], nombre=fila["nombre"], precio=fila["precio"])
        productos.append(producto)
    return productos


class Persona:
    def __init__(self, nombre, **kwargs):
        self.nombre = nombre
        super().__init__(**kwargs)

    def saludar(self):
        return f"Hola, soy {self.nombre}."


class Cliente:
    def __init__(self, cliente_id, **kwargs):
        self.cliente_id = cliente_id
        super().__init__(**kwargs)

    def datos_cliente(self):
        return f"Cliente ID: {self.cliente_id}"


class Empleado:
    def __init__(self, empleado_id, **kwargs):
        self.empleado_id = empleado_id
        super().__init__(**kwargs)

    def datos_empleado(self):
        return f"Empleado ID: {self.empleado_id}"


class ClienteEmpleado(Cliente, Empleado, Persona):
    def __init__(self, nombre, cliente_id, empleado_id):
        super().__init__(nombre=nombre, cliente_id=cliente_id, empleado_id=empleado_id)

    def datos_completos(self):
        return f"{self.saludar()} / {self.datos_cliente()} / {self.datos_empleado()}"


class Producto:
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"{self.nombre} (${self.precio:.2f})"


class Factura:
    _contador = 1

    def __init__(self, cliente_empleado):
        self.factura_id = Factura._contador
        Factura._contador += 1

        self.cliente_empleado = cliente_empleado
        self.fecha = datetime.datetime.now()
        self.items = []

    def agregar_producto(self, producto, cantidad):
        self.items.append((producto, cantidad))

    def total(self):
        return sum(p.precio * c for p, c in self.items)

    def imprimir_factura(self):
        print(f"\n======= FACTURA #{self.factura_id} =======")
        print(f"Fecha: {self.fecha.strftime('%Y-%m-%d %H:%M:%S')}")
        print(self.cliente_empleado.datos_completos())
        print("------------------------")
        for producto, cantidad in self.items:
            print(f"{producto.nombre} x{cantidad} = ${producto.precio * cantidad:.2f}")
        print("------------------------")
        print(f"TOTAL: ${self.total():.2f}")
        print("============================")

    def guardar_factura_txt(self, ruta="facturas"):
        os.makedirs(ruta, exist_ok=True)
        archivo = os.path.join(ruta, f"factura_{self.factura_id}.txt")
        with open(archivo, "w", encoding="utf-8") as f:
            f.write(f"FACTURA #{self.factura_id}\n")
            f.write(f"Fecha: {self.fecha.strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(self.cliente_empleado.datos_completos() + "\n")
            f.write("------------------------\n")
            for producto, cantidad in self.items:
                f.write(f"{producto.nombre} x{cantidad} = ${producto.precio * cantidad:.2f}\n")
            f.write("------------------------\n")
            f.write(f"TOTAL: ${self.total():.2f}\n")
        print(f"Factura guardada en: {archivo}")
        
if __name__ == "__main__":
    cliente = ClienteEmpleado("Jorge", "C123", "E456")
    p1 = Producto("P001", "Laptop", 4500.00)
    p2 = Producto("P002", "Mouse", 150.00)
    p3 = Producto("P003", "Teclado", 300.00)

    factura = Factura(cliente)
    factura.agregar_producto(p1, 1)
    factura.agregar_producto(p2, 2)
    factura.agregar_producto(p3, 1)

    factura.imprimir_factura()
    factura.guardar_factura_txt()
