"""
Instrucciones de la tarea:
El objetivo del ejercicio es crear un sistema de calificaciones, como sigue:
El usuario proporcionará un valor entre 0 y 10.
Si está entre 9 y 10: imprimir una A
Si está entre 8 y menor a 9: imprimir una B
Si está entre 7 y menor a 8: imprimir una C
Si está entre 6 y menor a 7: imprimir una D
Si está entre 0 y menor a 6: imprimir una F
cualquier otro valor debe imprimir: Valor incorrecto
Por ejemplo:
Proporciona un valor entre 0 y 10:
A
"""

cal = int(input("Calificacion del alumno: "))
mensajeA = None
print(cal)

if 9 <= cal <= 10:
    print(cal)
    mensajeA ="Aprobado, Felicidades"
    print(f'La calificacion es A, {mensajeA}')
elif 8 <= cal < 9:
    mensajeA = "Aprobado, pudo ser mejor"
    print(f'La calificacion es B, {mensajeA}')
elif 7 <= cal < 8:
    mensajeA = "Aprobado, pudo ser mejor"
    print(f'La calificacion es C, {mensajeA}')
elif 6 <= cal < 7:
    mensajeA = "Aprobado, pero de panzazo"
    print(f'La calificacion es D, {mensajeA}')
elif 0 <= cal < 6:
    mensajeA = "REPROBADO"
    print(f'La calificacion es F, {mensajeA}')
else:
    print("Valor no valido")



