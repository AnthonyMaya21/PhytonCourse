resultado = None
try:
    a = int(input('Primer número: '))
    b = int(input('Segundo número: '))
    resultado = a/b
#except ZeroDivisionError as e:
#    print(f'ZeroDivisionError - Ocurrió un error: {e} , {type(e)}')
#except TypeError as e:
#    print(f'TypeError - Ocurrió un error: {e} , {type(e)}')
# al poner la clase Exception no es necesario poner cada una 
# de las hijas a la mas generica 


except Exception as e:
    print(f'Exception - Ocurrió un error: {e} , {type(e)}')
else:
    print('No encontro ningun problema ') # Si no se encuentra ningun problema 
finally:
    print('Ejecución del bloque finally') # Independientemente si hay o no excepcion

print(f'Resultado: {resultado}')
print('Continuamos...')