def slice_simple():
    """Dada la variable texto = "Awesome", imprime distintas secciones de la cadena."""
    texto = "Awesome"
    
    # 1. Los primeros 3 caracteres en minúsculas
    print(texto[:3].lower())
    
    # 2. Los caracteres desde la posición 2 hasta la 4 (inclusive)
    print(texto[2:5].lower())
    
    # 3. El texto completo en minúsculas
    print(texto.lower())
