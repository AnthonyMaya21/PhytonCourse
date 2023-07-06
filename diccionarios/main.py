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
