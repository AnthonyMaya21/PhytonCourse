# dada la sig tupla
# crear una lista que solo incluya los numeros menores a 5

tupla = (13, 1, 8, 3, 2, 5, 8)

lista = []

i = len(tupla)

print(i)

for x in tupla:
    if x < 5:
        lista.append(x)

print(lista)