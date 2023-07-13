from FiguraGeometrica import FiguraGeometrica
from Color import Color

class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, ancho, alto) -> None:
       # super().__init__(ancho, alto)
       FiguraGeometrica.__init__(self, alto, alto)
       Color.__init__(self, color)
    
    def calcular_area(self):
        return self.alto * self.ancho
