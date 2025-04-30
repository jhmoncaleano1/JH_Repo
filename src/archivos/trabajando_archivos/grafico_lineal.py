import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data\\pedos.csv")
#Probamos si lo lee:
#print(df)
#creando el grafico
sns.lineplot(x="fecha",y="pedos",data=df)

#Creando un punto para resaltar en el mas grande 01-09,17
plt.plot("01-09",17,"o")

#mostrando el grafico
plt.show()
