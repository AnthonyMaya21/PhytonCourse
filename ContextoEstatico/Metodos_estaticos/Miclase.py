class Miclase: 

    variable_clase = 'Valor variable de clase'


    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia
    


    @staticmethod 
    def metodo_estatico():
        print(Miclase.variable_clase)


Miclase.metodo_estatico()