class celular:
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
        
    def llamar(self):
        print(f'Estas haciendo una llamada desde un:  {self.modelo}')
        
    def colgar(self):
        print(f'Estas colgando una llamada desde un:  {self.modelo}')   
    
celular1 = celular("Samsung","S23","48MP")
celular2 = celular("Apple","Iphone","96MP")

# no necesita indicar el print
celular2.llamar()