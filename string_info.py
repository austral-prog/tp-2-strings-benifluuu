def string_info():
    """Dada la variable palabra = "Programacion", imprime información detallada
    sobre la cadena utilizando f-strings y operaciones de strings.
    """
    palabra = "Programacion"
    
    # 1. Imprimir la palabra original
    print(f"Palabra: {palabra}")
    
    # 2. Imprimir su longitud usando len()
    print(f"Longitud: {len(palabra)}")
    
    # 3. Imprimir la primera letra usando el índice 0
    print(f"Primera letra: {palabra[0]}")
    
    # 4. Imprimir la última letra usando el índice -1
    print(f"Ultima letra: {palabra[-1]}")
    
    # 5. Imprimir la palabra repetida 3 veces con el operador *
    print(f"Repetida: {palabra * 3}")
    
    # 6. Imprimir la palabra decorada sumando los asteriscos a los lados
    print(f"Decorada: ***{palabra}***")