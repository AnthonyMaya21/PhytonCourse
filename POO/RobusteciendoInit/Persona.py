class Persona:
    def __init__(self, nombre, apellido, edad, *valores, **terminos):  # declaramos atributos
        # Ser pueden pasar duplas y diccionarios a una clase respetando el formato de estos
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.valores = valores
        self.terminos = terminos

    def mostrar_detalle(self):  # declaramos metodos
        print(f'Persona: {self.nombre} {self.apellido} {self.edad} {self.valores} {self.terminos}')

persona1 = Persona('Juan', 'Perez', 30, 2, 3, 4, 5, 6, a='arbol', b='barco')
persona1.mostrar_detalle()

# Se pueden modificar los atributos de una clase dirrectamente pero no es recomendable

persona2 = Persona('Ale', 'Laguna', 25)
persona2.mostrar_detalle()
