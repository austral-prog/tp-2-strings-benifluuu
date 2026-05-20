def check_vowels():
    # 1. Leer el nombre desde la entrada estándar
    nombre = input()
    
    # 2. Convertir a minúsculas para asegurar que la búsqueda no falle con mayúsculas
    nombre_min = nombre.lower()
    
    # 3. Verificar la existencia de cada vocal usando el operador 'in'
    # e imprimir los resultados usando f-strings
    print(f"Contiene a: {'a' in nombre_min}")
    print(f"Contiene e: {'e' in nombre_min}")
    print(f"Contiene i: {'i' in nombre_min}")
    print(f"Contiene o: {'o' in nombre_min}")
    print(f"Contiene u: {'u' in nombre_min}")