# ejercicio 1
def imrpimirdec(numero):
    if numero >= 1:
        print(numero)
        imrpimirdec(numero - 1)
    elif numero == 0 :
        return
    elif numero < 0:
        print('Valor incorrecto..')


# numero = int(input("Dame un numero: "))
# resultado = imrpimirdec(numero)
# print(resultado)

imrpimirdec(5)
