def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total."""
 
 
    Precio = input("Precio: ")
    print("Precio:",Precio)
    Descuento = input("descuento: ")
    print("Descuento:",Descuento)
    Cantidad = int(input())
    Precio_con_descuento = int(Precio) - (float(Descuento))
    print("Precio con descuento:", float(Precio_con_descuento))
    Precio_total = Precio_con_descuento * Cantidad
    print("Total:", Precio_total)

 
 
 
 
    pass

#casting()