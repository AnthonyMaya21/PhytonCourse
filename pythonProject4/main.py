# EJERCICIO EDAD

edad = int(input("Proporciona tu edad: "))
mensaje = None

if 0 <= edad < 10:
    mensaje = "La infancia es increíble..."
    print(f'Tu edad es {edad} , {mensaje} ')
elif 10 <= edad < 20:
    mensaje = "Muchos cambios y mucho estudio... "
    print(f'Tu edad es {edad} , {mensaje} ')
elif 20 < edad <= 30:
    mensaje = "Amor y comienza el trabajo..."
    print(f'Tu edad es {edad} , {mensaje} ')
else:
    mensaje = "Etapa de vida no reconocida"
    print(mensaje)
