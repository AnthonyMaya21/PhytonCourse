class Miclase: 

    variable_clase = 'Valor variable de clase'


    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia
    


    @staticmethod 
    def metodo_estatico():
        print(Miclase.variable_clase)
        # no puede accesar directamente a las variables de clase 


    @classmethod
    def metodo_clase(cls):
        # Recibe le parametro clase 
        print(cls.variable_clase)

Miclase.metodo_clase()
