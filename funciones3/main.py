#def sumar(a: int = 0, b:int = 0 ) -> int:

def sumar(a= 0, b=0): #valores por defecto de una funcion
    return a + b
# return 'Hola mundo'

resultado = sumar()
print(f'Resultado sumar: {resultado}')


print(f'Resultado sumar: {sumar(8,2)}')
