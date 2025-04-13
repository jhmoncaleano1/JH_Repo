# app/operaciones.py
# Función tradicional con def
def sumar(a, b):
    return a + b

# Función con parámetros *args
def sumar_varios(*args):
    return sum(args)

# Función con parámetros **kwargs
def saludar_persona(**kwargs):
    nombre = kwargs.get('nombre', 'Usuario')
    return f"Hola, {nombre}!"

# Función lambda (función anónima)
multiplicar = lambda x, y: x * y