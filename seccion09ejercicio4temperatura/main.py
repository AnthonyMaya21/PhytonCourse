# grados celsius a Fahrenheint
def celcius_a_fahren(gradosC):
    resF = (gradosC * 1.8) + 32
    return resF


# grados Fahrenheint a celsius
def fahren_a_celcius(gradosF):
    resC = (gradosF - 32) / 1.8
    return resC


print("1. Convertir grados Celcius a Fahrenheint")
print("2. Convertir grados Fahrenheint a Celcius ")
op = int(input())

if op == 1:

    grados = float(input('Dame grados Celcius: '))
    resultado = celcius_a_fahren(grados)
    print(f'{grados} C a F: {resultado:2}')
elif op == 2:
    grados = float(input('Dame Fahrenheint: '))
    resultado = fahren_a_celcius(grados)
    print(f'{grados} F a C: {resultado:2}')
else:
    print("Opcion no valida")
