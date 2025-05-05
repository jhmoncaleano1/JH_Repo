class Persona:
    def __init__(self, nombre, **kwargs):
        print("Inicializando Persona")
        self.nombre = nombre
        super().__init__(**kwargs)

    def saludar(self):
        return f"Hola, soy {self.nombre}."


class Cliente(Persona):
    def __init__(self, cliente_id, **kwargs):
        print("Inicializando Cliente")
        self.cliente_id = cliente_id
        super().__init__(**kwargs)

    def datos_cliente(self):
        return f"Cliente ID: {self.cliente_id}"


class Empleado(Persona):
    def __init__(self, empleado_id, **kwargs):
        print("Inicializando Empleado")
        self.empleado_id = empleado_id
        super().__init__(**kwargs)

    def datos_empleado(self):
        return f"Empleado ID: {self.empleado_id}"


class ClienteEmpleado(Cliente, Empleado):
    def __init__(self, nombre, cliente_id, empleado_id):
        print("Inicializando ClienteEmpleado")
        super().__init__(nombre=nombre, cliente_id=cliente_id, empleado_id=empleado_id)

    def datos_completos(self):
        return f"{self.saludar()} / {self.datos_cliente()} / {self.datos_empleado()}"


# ----- Ejecución -----
if __name__ == "__main__":
    persona = ClienteEmpleado("Jorge", "C123", "E456")
    print(persona.datos_completos())

    print("\nOrden de resolución de métodos (MRO):")
    for cls in ClienteEmpleado.__mro__:
        print(cls)
