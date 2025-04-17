#falto el profe y la clase la van a armar los niños
#el menor es asistente y el mayo es el profesor

#pedir nombre y edad de los que vinieron a clase, ordenarlo y sacar mayo y menor
def obtener_compañeros(cantidad_de_compañeros):
    compañeros = []
    for i in range(cantidad_de_compañeros):
        nombre = input("Ingrese el nombre del compañero: ")
        edad = input("ingrese la edad del compañero: ")
        compañero = (nombre,edad)
        compañeros.append(compañero)
    compañeros.sort(key=lambda x:x[1])
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    return asistente,profesor
asistente,profesor = obtener_compañeros(5)

print(f"El profesor es: {profesor} y su asistente es {asistente} ")

