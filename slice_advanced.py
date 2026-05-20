def slice_advanced():
    """Lee un texto mediante input() e imprime los caracteres desde la posición 4
    en adelante, de dos en dos.
    """
    # 1. Leer el texto de la entrada estándar
    texto = input()
    
    # 2. Aplicar el slicing arrancando en el índice 4, hasta el final, con paso 2
    resultado = texto[4::2]
    
    # 3. Imprimir el fragmento obtenido
    print(resultado)