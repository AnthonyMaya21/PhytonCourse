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

    def metodo_instancia(self):
        self.metodo_clase()
        self.metodo_estatico()
        print('Desde metodo instancia', self.variable_clase)
        print('Desde metodo instancia', self.variable_instancia)

Miclase.metodo_clase()
miObjeto1 = Miclase('Valor varible instancia')
miObjeto1.metodo_clase()
miObjeto1.metodo_instancia()
