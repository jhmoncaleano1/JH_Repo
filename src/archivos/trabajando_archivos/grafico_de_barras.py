import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data\\jh_ingresos.csv")
#Probamos si lo lee:
#print(df)
#creando el grafico
#sns.barplot(x="fuente",y="ingresos",data=df)

#Grafico con barras de colores ;)
sns.barplot(x="fuente", y="ingresos", hue="fuente", data=df, dodge=False, palette="tab10")

#vamos a totalizar los ingresos
total_ingresos = df['ingresos'].sum()
#y mostraos el total:
print(f"Eltotal de ingresos es de :   $ {total_ingresos}  USD")


#mostrando el grafico
plt.show()
