class estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        
    def estudiar(self):
        print("Estudiando....")    
#input de datos

nombre = input("Digame su nombre:  ")
edad = input("Digame su edad:  ")
grado = input("Digame su grado:  ")
        
estudiante = estudiante(nombre,edad,grado)

print(f"""
      Datos del estudiante: \n\n
      Nombre: {estudiante.nombre}  \n
      Edad : {estudiante.edad}  \n
      Grado : {estudiante.grado} \n
      """)
#Este while sigue preguntando hasta tener los datos correctos en ed def estudiar
while True:
    estudiar = input()
    if (estudiar.lower() == "estudiar"):
        estudiante.estudiar()
    