# Ejercicio 1. Iterar un rango de 0 a 10 e imprimir números divisibles entre 3

print("rango de 0 a 10 con numeros divisibles entre 3 ")
for i in range(11):
    if (i % 3 == 0 ):
        print(i)



# Ejercicio 2. Crear un rango de numeros de 2 a 6, e imprimelos
print("rango de 2 a 6 ")
rango = range(2,7)
for x in rango:
    print(x)

# Ejercicio 3. Crear un rango de 3 a 10, pero con incremento de 2 en 2, en lugar de 1 en 1


print("rango con valores de inicio = 3 , FIN 10 , incremento = 2")

rango = range(3, 11, 2)
for y in rango:
    print(y)