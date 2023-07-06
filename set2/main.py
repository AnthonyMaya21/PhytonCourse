# DICCIOANRIO (key, value)
diccionario = {
    'IDE':'Integrated Development Environment',
    'OPP': 'Object Oriented Programming',
    'DBMS': 'Database Management System'
}
print(diccionario)
#largo
print(len(diccionario))

# ACCEDER A UN ELEMENTO
print(diccionario['IDE'])
# OTRA FORMA DE RECUPERAR UN ELEMENTO
print(diccionario.get('OPP'))

#   modificando elementos
diccionario['IDE'] = ' deployment enviroment'

print(diccionario)


# parte 2

# Recorrer elementos

for termino in diccionario:
    print(termino)

# recorrer key y dato

for termino, valor in diccionario.items():
    print(termino, valor)

# recuperar solo llaver

for termino in diccionario.keys():
    print(termino)



# recuperar solo valores

for valor in diccionario.values():
    print(valor)

# comprobar existencia de algun elemento
print('IDE' in diccionario)

# print('IDe' in diccionario) regresa fals si no esta

# agregar un elemento

diccionario['PK'] = 'Primary Key'
print(diccionario)



# remover  un elemento

diccionario.pop('DBMS')
print(diccionario)

# limpiar
diccionario.clear()
print(diccionario)

#eliminar por completo

del diccionario
print(diccionario)




