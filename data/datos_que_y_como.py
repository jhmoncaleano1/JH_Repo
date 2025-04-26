import csv

with open("archivos\\datos.csv") as df:
    reader = csv.reader(df)
    for row in reader:
        print(row)
        
        
   # print(csv.reader(df))

#utilizando la funcion read_csv para leer archivos csv
# df:data frame / pd : pandas
#df = pd.read_csv("archivos\\datos.csv")
#df2 = pd.read_csv("archivos\\datos.csv") # para concatenar

#obteniendo los datos de la columna nombre
#nombres = df["nombre"]


print(df)
