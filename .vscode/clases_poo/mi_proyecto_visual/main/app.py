from funciones.operaciones import sumar, multiplicar, cuadrado
from funciones.argumentos import mostrar_args, mostrar_kwargs

print("Suma:", sumar(10, 5))
print("Multiplicación:", multiplicar(10, 5))
print("Cuadrado (lambda):", cuadrado(6))

print(mostrar_args(1, 2, 3, "hola"))
print(mostrar_kwargs(nombre="Jorge", edad=30))
