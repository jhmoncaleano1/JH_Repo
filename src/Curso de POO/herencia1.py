class persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        
# definimos el metodo hablar        
    def hablar(self):
        print("Hola, estoy hablando")
        
#hereda de persona y tiene atributos propios :         
class empleado(persona):
    def __init__(self,nombre,edad,nacionalidad,trabajo,salario):
       super().__init__(nombre,edad,nacionalidad)
       self.trabajo = trabajo
       self.salario = salario
        
Empleado1 = empleado("Roberto",43,"colombiano","google",12000000)

#Llamamos el programa hablar() de la clase persona

Empleado1.hablar()
print(Empleado1.nombre)