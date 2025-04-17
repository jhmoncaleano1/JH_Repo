diccionario = {
    "nombre":"Jorge H",
    "apellido":"Moncaleano",
    "saldo":1600000
}
print(diccionario)
#imprime cada clave
print("________________________________") 
print("claves")
for key in diccionario:
    print(key)
 #para imprimir clave y valor
print("________________________________") 
print("clave, valor")  
for key in diccionario.items():
    print(key) 
else:    
    print("________________________________")   
 #extrayendo los datos
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]

    print(f"La clave es : {key} y el valor es {value}")
    
#Ejemplo sacando exepciones de la lista if/continue
print("========================________________________________") 
frutas = ["banana","manzana","ciruela","pera","naranja","grandilla","uva"]
cadena = "Hola Jorge H"
numeros = [2,5,8,10]
for fruta in frutas:
    if fruta == 'manzana' :
        continue
    print(f'me voy a comer una {fruta}')  
    
print("========================___========================")
#recorrer una cadena caracter por caracter
for caracter in cadena:
    print(caracter)
print("========================___========================")
#Ahora la lista con operacion
numeros_duplicados = list()
for numero in numeros:
    numeros_duplicados.append(numero*2)
print(numeros_duplicados)  
print("========================___========================")
# el for en una sola linea
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados) 
    
    