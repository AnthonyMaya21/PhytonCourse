try:
    archivo = open('prueba.txt', 'r',encoding='utf8')
    #print(archivo.read())

    # Leer algunos caracteres 
    print(archivo.read(5))
    print(archivo.read(3))

    # leer lineas completas 

    print(archivo.readline())
    print(archivo.readline())

  




except Exception as e:
    print(f'Exception - Ocurrió un error: {e} , {type(e)}')

finally:
    archivo.close()
   