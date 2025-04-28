#              para evitar caracteres extraños: encoding="UTF-8" al final
archivo_sin_leer = open("archivos\\texto_para_python.txt",encoding="UTF-8")
#             el archivo solo abre una vez, hay que cerrlo al final con close
#                  leer el archivo completo:
#print(archivo_sin_leer.read())

#                  leer line por linea:
#lineas = archivo_sin_leer.readlines()
#                  cada linea termina con \n

#                  para leer una sola linea:
linea = archivo_sin_leer.readline()

print(linea)
archivo_sin_leer.close()
