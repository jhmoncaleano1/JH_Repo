import pandas as pd

#utilizando la funcion read_csv para leer archivos csv
# df:data frame / pd : pandas
df = pd.read_csv("data\\datos.csv")
df2 = pd.read_csv("data\\datos.csv") # para concatenar

#obteniendo los datos de la columna nombre
nombres = df["nombre"]

print(nombres)