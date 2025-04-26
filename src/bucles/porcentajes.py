cd documentos
def calcular_porcentajes():
    procesos = {}  # Diccionario para almacenar los autores y sus horas

    # Solicitar datos de forma interactiva
    while True:
        autor = input("Ingrese el nombre del autor (o 'fin' para terminar): ")
        if autor.lower() == "fin":
            break
        try:
            horas = float(input(f"Ingrese la duración en horas para {autor}: "))
            procesos[autor] = horas
        except ValueError:
            print("Error: Ingrese un número válido para las horas.")

    # Calcular total de horas
    total_horas = sum(procesos.values())

    # Mostrar resultados
    print("\nPorcentajes de duración:")
    for autor, horas in procesos.items():
        porcentaje = (horas / total_horas) * 100
        print(f"{autor}: {horas} horas ({porcentaje:.2f}%)")

# Ejecutar la función
calcular_porcentajes()
