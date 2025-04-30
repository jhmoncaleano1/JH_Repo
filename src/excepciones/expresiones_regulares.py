import re

#Expresiones regulares, son texto y se usan para buscar cadenas u ocurrencias

texto = '''Hola maestro esta es la cadena 1. Como estas mi capitan
Esta es la linea 2662598 de texto.
Esta es la linea 2 de texto.
Y esta es la final (linea 3) definitiva mi capitan'''

#Haciendo busqueda simple)

#\d -> busca digitos de 0 - 9
#resultado = re.findall(r"\d" ,texto)

#\D -> busca todo menos digitos de 0 - 9
#resultado = re.findall(r"\D" ,texto)

#\w -> busca caracteres alfanumericos [a-z A-Z  0-9 _]
#resultado = re.findall(r"\w" ,texto)

#\W -> busca todo menos caracteres alfanumericos [a-z A-Z  0-9 _]
#resultado = re.findall(r"\W" ,texto)

#\s -> busca espacios en blanco -> espacios, tabs, salto de linea
#resultado = re.findall(r"\s" ,texto)

#\S -> busca todo, menos espacios en blanco -> espacios, tabs, salto de linea
#resultado = re.findall(r"\S" ,texto)

#. -> busca todo menos salto de linea
#resultado = re.findall(r"." ,texto)
#\n -> busca salto de linea
#resultado = re.findall(r"\n" ,texto)

