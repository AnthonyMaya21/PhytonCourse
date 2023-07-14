from Empleado import Empleado 
from Gerente import Gerente

def imprimir_detalles(Objeto):
    # print(Objeto)
    print(type(Objeto))
    print(Objeto.mostrar_detalles())
    if isinstance(Objeto, Gerente):
         print(Objeto.departamento)



empleado = Empleado('Juan', 5000)
imprimir_detalles(empleado)


gerente2 = Gerente('Antonio', 7500, 'Sistemas')

imprimir_detalles(gerente2)


