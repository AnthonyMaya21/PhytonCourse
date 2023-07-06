def listaNombres(*nombres): # tambien se puede poner *args
    for nombre in nombres:
        print(nombre)

listaNombres('OptimusPrime', 'Jazz', 'Ironhide', 'Bumblebee')
listaNombres('Laura', 'Carlos')