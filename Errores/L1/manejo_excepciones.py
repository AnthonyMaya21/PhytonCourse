a = 10 
b = 0 
try : 
    resultado = a/b  
except Exception as error:
    
# except ZeroDivisionError as error  (solo cacha arrores de division entre cero) 
    print(f'Ocurrio un error: {error}')
