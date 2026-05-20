def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total."""
    # 1. Leer los datos desde la entrada estándar
    precio_str = input()
    descuento_str = input()
    cantidad_str = input()
    
    # 2. Convertir cada variable al tipo numérico correcto (Casting)
    precio = int(precio_str)          # "texto que representa un entero"
    descuento = float(descuento_str)  # "texto que representa un decimal"
    cantidad = int(cantidad_str)      # "texto que representa un entero"
    
    # 3. Realizar los cálculos matemáticos (Resta directa del valor)
    precio_con_descuento = precio - descuento
    total = precio_con_descuento * cantidad
    
    # 4. Mostrar los resultados usando f-strings con el formato exacto
    print(f"Precio: {precio}")
    print(f"Descuento: {descuento}")
    print(f"Precio con descuento: {precio_con_descuento}")
    print(f"Total: {total}")