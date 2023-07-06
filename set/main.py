#set

planetas = {'Marte', 'Jupiter', 'Venus'}
print(planetas)
# largo de un set }
print(len(planetas))

# revisar si un elemento esta presente

print('Marte' in planetas)# retorna true
print('Martes' in planetas)# retorna false si no esta

#agregar un elemento, sin orden

planetas.add('Tierra')
print(planetas)

#No se pueden duplicar elementos

planetas.add('Tierra')


planetas.remove('Tierra')
print(planetas)

#eliminar elemento sin arrojar error
planetas.discard('Jupiter')
print(planetas)

planetas.clear()
print(planetas)

#eliminar el set

del planetas
print(planetas)


