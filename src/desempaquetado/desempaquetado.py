#datos en  una tupla
datos_tupla = ("Jorge", "Hernan", 1635000)
#datos_lista
datos_lista = ["Jorge", "Hernan", 1635000]
#desempaquetado
nombret ,MNt, saldot = datos_tupla
nombrel ,MNl, saldol = datos_lista
#imprimiendo resultados
print (saldot, saldol)
#crear una tupla funcion tuple
tupla = tuple(["Jorge", "Hernan", 1635000])
print (tupla)
#crear tupla sin funcion (sin parentesis)
tupla_simple = "Jorge", "Hernan", 1635000
print (tupla_simple)

#para conjuntos set()
conjunto = set(["Jorge", "Hernan"])

print (conjunto)

#creando diccionarios funcion dict()
diccionario = dict(nombre="Jorge H",apellido="Moncaleano")
# o se puede crear {'nombre':"Jorge H",'apellido'="Moncaleano"} 