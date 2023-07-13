from Cuadrado import Cuadrado


print('Creaccion Objeto cuadrado'.center(50,'-'))

cuadrado1 = Cuadrado(lado=5, color='rojo')

print(f'Calculo area cuadrado: {cuadrado1.calcular_area()}')
print(cuadrado1)


from Rectangulo import Rectangulo

print('Creaccion Objeto Rectangulo'.center(50,'-'))

rectangulo1 = Rectangulo(ancho=5 ,lado= 3, color= "amarillo")
print(f'Calculo area rectangulo: {rectangulo1.calcular_area()}')
print(rectangulo1)


