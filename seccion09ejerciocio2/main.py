"""
Crear una función para multiplicar los valores recibidos de tipo numérico,
utilizando argumentos variables *args como parámetro de la función
y regresar como resultado la multiplicación de todos los valores pasados como argumentos.
"""


def multiplica_numero(*args):
    resultado = 1
    for valor in args:
        resultado *= valor
    return resultado


print(multiplica_numero(3, 3, 2, 3))
