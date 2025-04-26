import modulo_saludar

saludo = modulo_saludar.saludar("JorgeH")
print(saludo)
#___________________________________________
#podemos renombrar el modulo con AS
import modulo_saludar as m_saludar
saludo = m_saludar.saludar("JorgeH")
print(saludo)
#___________________________________________
#tambien podemos importar solo una funcion de el modulo
from modulo_saludar import saludar

saludo = saludar("JorgeH")
print(saludo)
