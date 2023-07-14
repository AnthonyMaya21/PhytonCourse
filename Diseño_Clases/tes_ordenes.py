from Orden import Orden
from Producto import Producto


producto1 = Producto('Camisa', 100.00)
producto2 = Producto('Pantalon', 150.00)
producto3 = Producto('Playera', 200)
producto4 = Producto('zapatos', 120)

productos1 = [producto1, producto2]
productos2 = [producto3, producto4]

orden1 = Orden(productos1)
orden1.agregar_producto(producto3)
orden1.agregar_producto(producto4)

print(orden1)
print(f'Total orden1: {orden1.calcular_total()}')


orden2 = Orden(productos1)
print(orden2)
print(f'Total orden2: {orden2.calcular_total()}')