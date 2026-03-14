'''FALTA IMPLEMENTAR:

    procesar_numero (basicamente la funcion que transforma un numero de una base a otra, 4 secciones, una para cada representacion)
    es_digito_valido (un checker simple que tenga un string(?) con los numeros validos para cada base, 4 secciones/variables again)
    crear e integrar una funcion que maneje lo de si el numero total se pasa del rango decimal permitido, [32, 126], yo creo q puede ir en el mismo procesar_numero)

    ocupa snake_case papu q es convencion internacional pa python xdd
    pone tu rol en el nombre del archivo

    y quiero ver el caso borde de si aparece un numero que se escapa de la base, se considera como un simbolo basura nomas? voy a preguntar en el foro

'''
with open("notas_dm.txt", "r") as arch:
    while True:
        caracter = archivo.read(1)
        if not caracter:
            break #Fin del archivo
        # 1- Prefijo?
        if caracter in ["*", "&", "#", "!"]:
            if acumulador:
                # Check y procesamiento por si ya se venia armando un numero
                procesar_numero(acumulador, base_actual)

            if caracter == "*": base_actual = 2
            elif caracter == "&": base_actual = 8
            elif caracter == "#": base_actual = 10
            elif caracter == "!": base_actual = 16

            acumulador = "" #Se limpia para acumular el nuevo numero
        
        # 2- Es digito valido para la base?
        elif base_actual is not None and es_digito_valido(caracter, base_actual):
            acumulador += caracter

        # 3- Es basura? (asumiendo que un numero invalido para la base tmb es basura)
        else: 
            if acumulador:
                procesar_numero(acumulador, base_actual)
                acumulador = ""
                base_actual = None 