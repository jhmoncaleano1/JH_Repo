#para no abrir y cerrar o dejar abierto
with open("archivos\\texto_para_python.txt",encoding="UTF-8") as archivo:
     print(archivo.read())
     #no es necesario cerrarlo al uas with open