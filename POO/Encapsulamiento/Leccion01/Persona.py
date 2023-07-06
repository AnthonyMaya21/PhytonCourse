class Persona:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre # encapsulamiento "sencillo"
        # self.__nombre = nombre  encapsulamiento doble y menos comun
        self.apellido = apellido
        self.edad = edad

    def mostrar_detalle(self):  # declaramos metodos
        print(f'Persona: {self._nombre} {self.apellido} {self.edad} ')

persona1 = Persona('Juan', 'Perez', 30)
persona1._nombre = 'Juan Carlos' # Es posible modificar aun encapsulado, pero no es recomendable
persona1.mostrar_detalle()


persona2 = Persona('Ale', 'Laguna', 25)
persona2.mostrar_detalle()
