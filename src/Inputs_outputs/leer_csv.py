import csv
#Recomendacion: estos archivos es mejor leerlos con Pandas
with open("data\\datos.csv") as archivo:
    reader = csv.reader(archivo)
    for row in reader:
        print(row)