def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """

    gasto = float(input("Ingrese el gasto: "))
    dinero_recibido = int(input("Ingrese el dinero recibido: "))

    print("Ingresar gasto:")
    print(gasto)
    print("Dinero recibido")
    print(dinero_recibido)
    print("")
    Vuelto = dinero_recibido - gasto
    Pesos = int(Vuelto)
    print("Vuelto")
    print("")
    print("Pesos:")
    print(Pesos)
    Centavos = round((Vuelto - Pesos)*100)
    print("Centavos:")
    print(Centavos)













    pass


#change()
