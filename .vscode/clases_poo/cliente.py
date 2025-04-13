# cliente.py
class Cliente:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo

    def __str__(self):
        return f"Cliente: {self.nombre}, Correo: {self.correo}"