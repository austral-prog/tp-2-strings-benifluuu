def ficha():
    # 1. Leer todas las entradas necesarias
    nombre_sucio = input()
    email_sucio = input()
    nota1_str = input()
    nota2_str = input()
    nota3_str = input()

    # 2. Procesamiento del Nombre y Apellido
    nombre_limpio = nombre_sucio.strip().title()
    # Para separar nombre y apellido y armar las iniciales/usuario, buscamos el espacio intermedio
    pos_espacio = nombre_limpio.find(" ")
    
    # Iniciales: primera letra del nombre [0] y primera letra del apellido [pos_espacio + 1]
    inicial_nombre = nombre_limpio[0]
    inicial_apellido = nombre_limpio[pos_espacio + 1]
    iniciales = inicial_nombre + inicial_apellido

    # Usuario: apellido.nombre en minúsculas
    nombre_solo = nombre_limpio[:pos_espacio].lower()
    apellido_solo = nombre_limpio[pos_espacio + 1:].lower()
    usuario = f"{apellido_solo}.{nombre_solo}"

    # Código secreto: el nombre limpio completo invertido y en mayúsculas
    codigo_secreto = nombre_limpio[::-1].upper()

    # 3. Procesamiento del Email
    email_min = email_sucio.lower()
    email_valido = "@" in email_min
    
    # Extraer dominio: buscamos el carácter "@" y tomamos todo lo que está después
    pos_arroba = email_min.find("@")
    dominio = email_min[pos_arroba + 1:]

    # 4. Procesamiento de Notas y Operaciones Matemáticas
    n1 = int(nota1_str)
    n2 = int(nota2_str)
    n3 = int(nota3_str)
    
    suma = n1 + n2 + n3
    promedio = suma / 3
    promedio_entero = suma // 3

    # 5. Impresión de la ficha con el formato exacto requerido
    # Encabezado multilínea
    encabezado = """========================
    FICHA DEL ALUMNO
========================"""
    print(encabezado)

    # Datos del alumno procesados
    print(f"Nombre: {nombre_limpio}")
    print(f"Email: {email_min}")
    print(f"Caracteres en nombre: {len(nombre_limpio)}")
    print(f"Iniciales: {iniciales}")
    print(f"Usuario: {usuario}")
    print(f"Email valido: {email_valido}")
    print(f"Dominio: {dominio}")
    print(f"Nombre para archivo: {nombre_limpio.replace(' ', '_')}")
    print(f"Cantidad de a: {nombre_limpio.lower().count('a')}")
    print(f"Codigo secreto: {codigo_secreto}")
    
    # Notas y cálculos numéricos
    print(f"Nota 1: {n1}")
    print(f"Nota 2: {n2}")
    print(f"Nota 3: {n3}")
    print(f"Suma: {suma}")
    print(f"Promedio: {promedio}")
    print(f"Promedio entero: {promedio_entero}")
    
    # Cierre decorativo con repetición de string
    print("=" * 24)