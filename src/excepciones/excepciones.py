def sumar_dos():
    while True:
        a = input("Numero 1: ")
        b = input("Numero 2: ")
        try:
            resultado = int(a) + int(b)
        except:
            print("el dato debe ser numerico")
        else:
            break    
    return resultado

print(sumar_dos())