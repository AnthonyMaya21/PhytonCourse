#definir tuplas
frutas = ("naraja", "platano", "limon")

print(frutas)

# saber el rango

print(len(frutas))

# acceder a un elemento

print(frutas[0])

# navegacion inversa
print(frutas[-1])

#acceder a un rango
print(frutas[0:2]) # sin inclluir el ultimo indice


for fruta in frutas:
    # print(fruta)
    print(fruta, end=' ')

# cambiar vaolor tupla
# frutas[0 = "Pera"


frutasLista = list(frutas)
frutasLista[0] = "Pera"
frutas = tuple(frutasLista)
print('\n', frutas)


#eliminar la tupla

print('\n', frutas)
