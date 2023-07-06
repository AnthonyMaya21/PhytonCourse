class Persona:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre # encapsulamiento "sencillo"
        # self.__nombre = nombre  encapsulamiento doble y menos comun
        self.apellido = apellido
        self.edad = edad

    @property
    def nombre(self):
        print("Llamando metodo get")
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
        print("Llamando metodo set")


    def mostrar_detalle(self):  # declaramos metodos
        print(f'Persona: {self._nombre} {self.apellido} {self.edad} ')

persona1 = Persona('Juan', 'Perez', 28)
print(persona1.nombre)
persona1.nombre = 'Juan Carlos'
print(persona1.nombre)

