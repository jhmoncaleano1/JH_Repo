def saludar():
    print("Hola buenos dias")
saludar()    

numeros = [4,7,42,1]
#sum : suma todos los valores contenidos en la tupla
suma_total = sum(numeros)

print(numeros)
saludar()

#funcion con parametros:
def saludar(nombre, sexo):
    sexo = sexo.lower()
    if (sexo == "mujer"):
        adjetivo = "reina"
    elif (sexo == "hombre"):
        adjetivo = "Titan"
    else:
        adjetivo = "que tal eso"        
    print(f"Hola {nombre}, mi {adjetivo},  como estas")
    

saludar("claudia","mujer")    

#crear funcion que retorna vLORES( UNA CLAVE)
def crear_contraseña_random(num):
    chars = "abcdefghij"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contraseña
   
    
pasword = crear_contraseña_random(1)
frase = f"La Contraseña resultante es : {password}
print(frase)    