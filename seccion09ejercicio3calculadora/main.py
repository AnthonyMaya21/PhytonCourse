"""
Ejercicio: Calculadora de Impuestos
Crear una función para calcular el total de un pago incluyendo un impuesto aplicado.
# Formula: pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
"""


def calcular_impuesto(preciosin, impuesto):
    pago_total = preciosin + (preciosin * (impuesto / 100))
    return pago_total


precio = float(input("Dame el pago sin impuesto: "))
imp = float(input("Dame el impuesto: (%) "))

print(calcular_impuesto(precio, imp))
