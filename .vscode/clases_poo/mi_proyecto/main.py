# main.py
from app.operaciones import sumar, sumar_varios, saludar_persona, multiplicar

# Llamada a la función de suma
resultado_suma = sumar(10, 20)
print(f"Resultado de suma: {resultado_suma}")

# Llamada a la función de suma con varios números
resultado_suma_varios = sumar_varios(1, 2, 3, 4, 5)
print(f"Suma de varios números: {resultado_suma_varios}")

# Llamada a la función de saludo con kwargs
saludo = saludar_persona(nombre="Carlos")
print(saludo)

# Llamada a la función lambda (multiplicar)
resultado_multiplicacion = multiplicar(5, 6)
print(f"Resultado de multiplicación: {resultado_multiplicacion}")
