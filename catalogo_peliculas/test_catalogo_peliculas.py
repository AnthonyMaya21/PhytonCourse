from dominio.Pelicula import Pelicula
from servicio.CatalogoPeliculas import CatalogoPeliculas as Cat

op = None

while op != 4: 
    try:
        print('Opciones: ')
        print('1. Agregar Peliculas')
        print('2. Listar peliculas')
        print('3. Eliminar archivo de peliculas')
        print('4. Salir')
        op = int(input(''))
    

        if op == 1:
            print('Agrega Pelicula'.center(25,'*'))
            nombre_pelicula = input('Ingresa el nombre de la pelicula: ')
            pelicula = Pelicula(nombre_pelicula)
            Cat.agregar_pelicula(pelicula)
        elif op == 2:
            print('Listar Pelicula'.center(25,'*'))
            Cat.listar_peliculas()
        elif op == 3:
            print('Elimnar pelicula'.center(25,'*'))
            Cat.eliminar_peliculas()
    except Exception as e:
        print(f'Ocurrio este error {e}')
        op = None

else: 
     print('Gracias vuelva pronto'.center(25,'*'))



