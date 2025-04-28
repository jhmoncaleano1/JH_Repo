# cambiar el tipo de datos de una columna
import pandas as pd
df = pd.read_csv("data\\datos.csv")

#convertir a string los datos de una columna
df['edad'] = df['edad'].astype(str)

#mostrar el tipo de datos del primer elemento de la columna edad
print(type(df['edad'][0]))

#reemplazando los datos "Alvarez" por "maestro"
df['apellido'].replace("Alvarez","maestro",inplace=True)

#eliminando filas con datos faltantes
df = df.dropna()

#eliminando filas repetidas
df = df.drop_duplicates()

#creando un CSV con el DataFrame resultante (limpio)
df.to_csv("data\\datos_limpios.csv")

#mostrando la columna apellido
print(df['apellido'])