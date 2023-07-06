class Rectangulo:
    def __init__(self, base, altura ):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura


base = int(input("Dame la base: "))
altura = int(input("Dame la altura: "))

rec1 = Rectangulo(base,altura)

print(f'El area del rectangulo es de: {rec1.calcular_area()}')


base = int(input("Dame la base: "))
altura = int(input("Dame la altura: "))

rec2 = Rectangulo(base,altura)

print(f'El area del rectangulo es de: {rec2.calcular_area()}')