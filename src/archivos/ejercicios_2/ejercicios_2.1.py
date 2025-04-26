#Falto el profesor y los alumnos deben organizar la clase.
#Entrar la lista de alumnos con una funcion "def" que entra el numero de alumnos que vamos a usar
# la ordenamos y sacamos de la lista el 1o, menor como asistente y el ultimo, mayor, como profesor

#funcion para obtener asistente y profesor: (La funcion se llama con el numero de compañeros a trabajar)
def obtener_compañeros(cantidad_de_compañeros):
    
    #creando la lista de compañeros
    compañeros = []
    
    #ejecutando un for para pedir la informacion de cada compañero
    for i in range(cantidad_de_compañeros):
        nombre = input("Ingrese el nombre del compañero: ")
        edad = input("Ingrese edad del compañero: ")
        # la variable compañero coloco nombre,edad
        compañero = (nombre,edad)
        
        #el dato anterior lo agrego a la lista llamada compañeros y termino el for
        compañeros.append(compañero)
        
    #Los ordeno de menor a mayor por edad que es el segundo campo o sea : 0,1
    compañeros.sort(key=lambda x:x[1])    
    
    #compañeros devuelve una tupla con (nombre,edad) y accedemos al nombre (0) para definir asistente y profesor:
    asistente = compañeros[0][0] #el primer campo de la primera linea
    profesor = compañeros[-1][0] # el ultimo
    
    #retornamos una tupla del for ejecutado
    return asistente,profesor

#desempaquetamos lo que nos retorno la funcion

#ejecuto la funcion con valor 5
asistente,profesor = obtener_compañeros(5)

#mostrando resultados
print(f"El profesor es  :  {profesor} y su asistente es  : {asistente}")

        