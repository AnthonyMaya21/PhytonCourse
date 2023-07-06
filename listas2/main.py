#definir una lista de tipo str

nombres = ['Juan','Karla','Ricardo','Maria']
#Imprimir la lista nombres
print(nombres)
print(nombres[0])
print(nombres[1])
print(nombres[2])
# acceder a los elementos de manera inversa }
print(nombres[-1])
print(nombres[-2])

# Imprimir un rango
print(nombres[0:2]) # sin incluir el indice 2
# Ir del inicio de la lista al indice (sin incluirlo)
print(nombres[:3])
# desde el indice indicado hasta el final
print(nombres[1:])


# desde el indice indicado hastael final
print(nombres[1:])

# cambiar un valor
nombres[3] = 'Ivonne'

# imprimir valores

print(nombres)

#iterar una lista

for nombre in nombres:
    print(nombre)
else:
    print("No existen mas nombres en la lista")