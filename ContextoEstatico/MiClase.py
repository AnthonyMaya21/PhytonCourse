class MiClase:

    variables_clase = 'Valor variable clase'
    
    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia

print(MiClase.variables_clase)
# no es necesario instanciar un objeto para poder acceder 

miClase1 = MiClase('Valor Variable instancia')
print(miClase1.variable_instancia)
print(miClase1.variables_clase)


miClase2 = MiClase('Otro valor de variable instancia')
print(miClase2.variable_instancia)