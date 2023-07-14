class Persona2: 
    # variable de clase 
    contador_personas = 0

    @classmethod
    def generar_siguiente_valor(cls):
        cls.contador_personas += 1
        return cls.contador_personas

    def __init__(self, nombre, edad) :
     
        self.id_persona = Persona2.generar_siguiente_valor()
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'Persona2: [{self.id_persona} {self.nombre} {self.edad} ]'
    

persona1 = Persona2('Rafael', 25)
print(persona1)

persona21 = Persona2('Lilia', 26)
print(persona21)

persona3 = Persona2('Lucy', 10)
print(persona3)


Persona2.generar_siguiente_valor()

persona4 = Persona2('Juan', 30)
print(persona4)

print(f'Valor contador personas: {Persona2.contador_personas}')

