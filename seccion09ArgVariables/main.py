def listarTerminos(**terminos): #Puede ser keyword
    for llave, valor in terminos.items():
        print(f'{llave}: {valor}')

listarTerminos(IDE='iNTEGRATED Development Environment', PK='Primary key')
