#definir una lista de tipo str

nombres = ['Juan', 'Karla','Ricardo','Maria']
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

# PREGUNTAR EL LARGO DE UNA LISTA

print(len(nombres))

# agregar un nuevo elemento
nombres.append("Lorenzo")
print(nombres)
# insertar un elemento en un indice en especifico, los demas se recorren a la derecha

nombres.insert(1,"Octavio")
print(nombres)

#remover un elemento por valor se recorren a la izq

nombres.remove("Octavio")
print(nombres)

# elimina el ultimo elemento aagregado a la lista
nombres.pop()
print(nombres)

# eliminar un indice
del nombres[0]
print(nombres)

# limpirAR LISTa

nombres.clear()
print(nombres)

# borrar la lista por completo

del nombres
print(nombres)



