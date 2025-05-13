# main.py (en la raíz del proyecto)
import sys
import os
sys.path.append(os.path.abspath("src"))

from modelo_app import SistemaVentas

sistema = SistemaVentas()
sistema.cargar_datos("data/clientes.xlsx", "data/productos.xlsx")
factura = sistema.generar_factura("Juan Perez", [(101, 2), (102, 1)])
sistema.guardar_factura_txt("outputs/factura_juan.txt")
