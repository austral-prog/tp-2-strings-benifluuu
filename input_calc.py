def rectangle():
    """Lee base y altura de un rectángulo, calcula e imprime
    el área y el perímetro.
    """
    # 1. Leer la base y la altura desde la entrada estándar
    base_str = input()
    altura_str = input()
    
    # 2. Convertir los valores a enteros (Casting)
    base = int(base_str)
    altura = int(altura_str)
    
    # 3. Calcular el área y el perímetro
    area = base * altura
    perimetro = 2 * (base + altura)
    
    # 4. Imprimir los resultados con el formato exacto usando f-strings
    print(f"Base: {base}")
    print(f"Altura: {altura}")
    print(f"Area: {area}")
    print(f"Perimetro: {perimetro}")
