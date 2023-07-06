class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

persona1 = Persona('Juan', 'Perez', 30)
# print(persona1.nombre)
# print(persona1.apellido)
# print(persona1.edad)
print(f'Objeto persona 1: {persona1.nombre} {persona1.apellido} {persona1.edad}')

persona2 = Persona('Ale', 'Laguna', 25)
print(f'Objeto persona 2: {persona2.nombre} {persona2.apellido} {persona2.edad}')
