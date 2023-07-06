class Cubo:
    def __init__(self, alto, ancho, prof):
        self.alto = alto
        self.ancho = ancho
        self.prof = prof

    def volumen_cubo(self):
        return self.alto * self.ancho * self.prof


a = int(input("Dame el alto: "))
b = int(input("Dame el ancho: "))
c = int(input("Dame la profundidad: "))

volumen = Cubo(a, b, c)

print(f'El volumen del cubo es: {volumen.volumen_cubo()}')
