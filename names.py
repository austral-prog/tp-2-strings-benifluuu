def names():
    """Lee nombre y apellido, e imprime el nombre completo en distintos formatos:
    minúsculas, título, mayúsculas y con tabulador.
    """
    # Leer el nombre y el apellido por separado
    nombre = input()
    apellido = input()
    
    # Concatenar ambos con un espacio de por medio
    nombre_completo = nombre + " " + apellido
    
    # Imprimir en los formatos requeridos por los tests
    print(nombre_completo.lower())
    print(nombre_completo.title())
    print(nombre_completo.upper())
    print("\t" + nombre_completo.lower())
