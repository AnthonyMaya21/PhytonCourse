class Persona:
    def __init__(self, nombre, apellido, edad):  # declaramos atributos
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def  mostrar_detalle(self): # declaramos metodos
        print(f'Persona: {self.nombre} {self.apellido} {self.edad}')

persona1 = Persona('Juan', 'Perez', 30)
persona1.mostrar_detalle()

#Se pueden modificar los atributos de una clase dirrectamente pero no es recomendable

persona2 = Persona('Ale', 'Laguna', 25)
persona2.mostrar_detalle()
