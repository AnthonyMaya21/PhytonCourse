class Aritmetica:
    """
    Clase Aritmetica para realizar las operaciones de sumar, restar, etc
    """
    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB

    def sumar(self):
        return self.operandoA + self.operandoB
    def restar(self):
        return self.operandoA - self.operandoB
    def multiplicar(self):
        return self.operandoA * self.operandoB
    def dividir(self):
        return self.operandoA / self.operandoB

aritmetica1 = Aritmetica(5,3)
print(f'Suma: {aritmetica1.sumar()}')
print(f'Resta: {aritmetica1.restar()}')
print(f'Miltiplicacion: {aritmetica1.multiplicar()}')
print(f'Division: {aritmetica1.dividir():.2f}')

print('\n')
aritmetica2 = Aritmetica(10,5)

print(f'Suma: {aritmetica2.sumar()}')
print(f'Resta: {aritmetica2.restar()}')
print(f'Miltiplicacion: {aritmetica2.multiplicar()}')
print(f'Division: {aritmetica2.dividir():.2f}')
