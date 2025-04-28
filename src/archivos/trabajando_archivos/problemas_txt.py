# 2 listas, una con nombres y otra con apellidos
nombres = ["JorgeH","Lucas","Camilo","Pedro","Roberto"]
apellidos = ["Moncaleano","Dalto","Zing","Robertix","Perez"]

#Registrar est informacion en un archivo TXT de forma optima

with open("data\\nombres_y_apellidos.txt","w") as arch:
    arch.writelines("Los datos son:\n\n")
    [arch.writelines(f"Nombre: {n}\nApellido: {a}\n-------\n") for n,a in zip(nombres,apellidos)]
    
#for n,a in zip(nombres,apellidos):
#    arch.writelines(f"nombre: {n}\nApellido: {a}\n---------\n")
