class Persona:
    def __init__(self, nombre, apellido, edad):  # declaramos atributos
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def  mostrar_detalle(self): # declaramos metodos
        print(f'Persona: {self.nombre} {self.apellido} {self.edad}')

persona1 = Persona('Juan', 'Perez', 30)
persona1.mostrar_detalle()
# Agregar nuevo atributo solamente al objeto Persona1
persona1.telefono = "56325411"
# Persona.mostrar_detalle(persona1)   Llamaar a un metodon de una clase, pasando como argumento el objeto instanciado

print((persona1.telefono))



#Se pueden modificar los atributos de una clase dirrectamente pero no es recomendable

persona2 = Persona('Ale', 'Laguna', 25)
persona2.mostrar_detalle()

# print((persona2.telefono))