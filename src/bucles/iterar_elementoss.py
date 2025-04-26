animales = ["gato","perro","loro","cocodrilo"]
numeros = [68,81,45,24]
for animal in animales:
    print(f'Ahora la variable animal es : {animal}')
    
#Para recorrer 2 listas en paralelo deben tener misma cantidad de elementos

for numero,animal in zip(numeros,animales):
    print(f"recorriendo lista 1: {numero}")
    print(f"recorriendo lista 2: {animal}")

#forma correcta de recorrer una lista con su indice y el else
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f'el indice es : {indice} y el valor es : {valor}')
else:
    print("El bucle termino")
    