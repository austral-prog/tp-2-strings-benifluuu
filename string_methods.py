def string_methods():
    # Variables iniciales dadas en la consigna
    nombre = "   Grace Hopper   "
    frase = "Python es un gran lenguaje de programacion"
    multilinea = """Linea 1
Linea 2
Linea 3"""

    # 1. Operaciones de limpieza de espacios (strip, lstrip, rstrip)
    print(f"Strip: {nombre.strip()}")
    print(f"Lstrip: {nombre.lstrip()}")
    print(f"Rstrip: {nombre.rstrip()}")

    # 2. Modificaciones de mayúsculas y minúsculas (upper, lower, title)
    print(f"Upper: {frase.upper()}")
    print(f"Lower: {frase.lower()}")
    print(f"Title: {frase.title()}")

    # 3. Búsqueda de posiciones (find)
    print(f"Find: {frase.find('gran')}")

    # 4. Reemplazo de texto (replace)
    print(f"Replace: {frase.replace('programacion', 'desarrollo')}")

    # 5. Conteo de caracteres específicos (count)
    print(f"Count: {frase.count('a')}")

    # 6. Verificación de pertenencia (operador in)
    print(f"Contiene Python: {'Python' in frase}")
    print(f"Contiene Java: {'Java' in frase}")

    # 7. Slicing simple (Extraer "Python")
    # "Python" ocupa los primeros 6 caracteres de la frase (índices 0 al 5)
    print(f"Slice: {frase[0:6]}")

    # 8. Slicing con paso no contiguo ("Python" con paso 2)
    # De "Python", tomamos el índice 0 ('P'), el 2 ('t') y el 4 ('o')
    print(f"Paso: {frase[0:6:2]}")

    # 9. Slicing reverso
    # Usamos [5::-1] para invertir únicamente la palabra "Python" (del índice 5 al 0)
    print(f"Reverso: {frase[5::-1]}")

    # 10. f-string combinado
    print(f"Formato: {nombre.strip()} sabe {frase[0:6]}")

    # 11. String multilínea
    print(multilinea)