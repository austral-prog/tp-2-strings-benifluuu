def string_info():
    """Dada la palabra 'Programacion', imprime su longitud, primera y última letra,
    la palabra repetida 3 veces y decorada con '***'.
    """
    palabra = "Programacion"


    palabra = "Programacion"
    print("Palabra:", palabra)
    print("Longitud:",len(palabra))
    print("Primera letra:",palabra[0])
    print("Ultima letra:",palabra[11])
    print("Repetida:",palabra*3)
    print("Decorada:",f"***{palabra}***")


#string_info()