# al escribir, sobreescribe el archivo si existia o lo crea si no existia
with open("data\\nuevo_texto.txt",'w',encoding="UTF-8") as archivo:
#    archivo.write("primera linea de codigo")
    
    #tambien se pueden escribir 2 lineas
    archivo.writelines(["  - Hola maestro como estas\n","   -misericordia\n"])
    #Y agregar otras 2 lineas
    archivo.writelines(["  - No se porque dije eso\n","   -Yo tampoco\n"])
    
    # con 'a', agregamos
with open("data\\nuevo_texto.txt",'a',encoding="UTF-8") as archivo:
        archivo.write("jajaja la agregue al final")
        archivo.write("jajaja la agregue al final otra vex")