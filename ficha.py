def ficha():
    """Ejercicio integrador. Lee nombre, email y 3 notas, y genera una ficha
    de alumno aplicando: strip, title, lower, upper, int, len, find, slicing,
    reverse, replace, count, in, f-strings, strings multilínea y operaciones matemáticas.
    """
    # Ejercicio integrador: Generador de Ficha de Alumno
    #
    # Leer mediante input:
    #   1. Nombre completo (puede tener espacios extra y mayúsculas mezcladas)
    #   2. Email (puede tener mayúsculas)
    #   3. Tres notas (como texto, hay que convertirlas)
    #
    # Generar una ficha que incluya:
    #   - Encabezado decorativo usando un string multilínea con "="
    #   - Nombre limpio: sin espacios extra y con formato título
    #   - Email en minúsculas
    #   - Cantidad de caracteres del nombre
    #   - Iniciales: usar find para encontrar el espacio e indexar las letras
    #   - Usuario: apellido.nombre en minúsculas
    #   - Verificar si el email contiene @ 
    #   - Extraer el dominio del email
    #   - Nombre con guion bajo en vez de espacio
    #   - Contar las 'a' en el nombre
    #   - Código secreto: nombre invertido en mayúsculas
    #   - Las 3 notas, su suma, promedio y promedio entero
    #   - Cierre decorativo usando repetición de string ("=" * 24)
   
    print("========================")
    print(" "+ " "+ " ","ficha del alumno".upper())
    print("========================")
    Nombre = input("Nombre:").strip()
    Email = input("Email:")
    Notas = [(str(input("Nota 1:"))),(str(input("Nota 2:"))),(str(input("Nota 3:")))] 
    print("Nombre:",Nombre.title())
    print("Email:",Email.lower())
    print("Caracteres en nombre:",len(Nombre))
    print("Iniciales:", f"{Nombre[0].upper()}{Nombre[Nombre.find(" ")+1].upper()}",)
    print("Usuario:", f"{(Nombre[Nombre.find(" ")+1:]).lower()}.{(Nombre[0:Nombre.find(" ")]).lower()}")
    print("Email valido:", "@" in Email)
    print("Dominio:", Email.lower()[Email.find("@")+1:])
    print("Nombre para archivo:", Nombre.replace(" ","_").title())
    print("Cantidad de a:",Nombre.lower().count("a"))
    print("Codigo secreto:",Nombre.upper()[::-1])
    print("Nota 1:",Notas[0])
    print("Nota 2:",Notas[1])
    print("Nota 3:",Notas[2])
    print("Suma:",int(Notas[0])+int(Notas[1])+int(Notas[2]))
    print("Promedio:",(int(Notas[0])+int(Notas[1])+int(Notas[2]))/3)
    print("Promedio entero:", int((int(Notas[0])+int(Notas[1])+int(Notas[2]))/3))
    print("="*24)
   
   
    pass
