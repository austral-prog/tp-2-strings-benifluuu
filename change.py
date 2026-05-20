def change():
    # 1. Leer el gasto y convertirlo a float antes de imprimir el eco
    print("Ingresar gasto:")
    gasto_str = input()
    gasto = float(gasto_str)
    print(gasto) # Al imprimir el float, "67.40" se convierte en "67.4" automáticamente
    
    # 2. Leer y mostrar el dinero recibido
    print("Dinero recibido")
    dinero_str = input()
    dinero = int(dinero_str)
    print(dinero)
    
    # 3. Calcular el vuelto total y redondear
    vuelto_total = round(dinero - gasto, 2)
    
    # 4. Separar la parte entera (pesos) y la decimal (centavos)
    pesos = int(vuelto_total)
    centavos = round((vuelto_total - pesos) * 100)
    
    # 5. Imprimir los resultados con el formato exacto del test
    print("") 
    print("Vuelto")
    print("") 
    print("Pesos:")
    print(pesos)
    print("Centavos:")
    print(centavos)