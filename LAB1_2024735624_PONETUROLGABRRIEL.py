'''
FALTA IMPLEMENTAR:

    comentar funciones

    procesar_numero (basicamente la funcion que transforma un numero de una base (base_in) a decimal, y de decimal a la base que se pide (base_out))
        -en procesar_numero, ya hice la logica de base_in a decimal, tambien el checkeo de q el numero en decimal este entre 32 y 126 (inclusive) -> no estoy seguro de eso, hay q preguntar en el foro
        -falta la logica de decimal a base_out y el print con: (deja el print en la funcion, no en el main)
            1- el numero de valor (ya implementado con el global valores_extraidos)
            2- el valor transformado en base_out
            3- la representacion original en base_in (con su simbolo, ver runtime del pdf)
        -transformar los valores (no se si desde el decimal o que) a ASCII (NI PERRA IDEA COMO XDDD)
        -agregar el valor en ASCII al global msg_final
        -printear el msg_final

    en vola se me va algo, ocupa este espacio como bloc de notas asi puedo ver yo cuando me meta dsps de un commit tuyo

    RECUERDA COMMITEAR ANTES DE APAGAR EL PC

    ocupa snake_case papu q es convencion internacional pa python xdd
    pone tu rol en el nombre del archivo


'''

def es_digito_valido (digito, base): 
    if base == 2 and digito in "01": return True

    elif base == 8 and digito in "01234567": return True

    elif base == 10 and digito in "0123456789": return True

    elif base == 16 and digito in "0123456789ABCDEF": return True

def transformar_letra_entero (char):
    digitos = "0123456789ABCDEF"
    entero = 0
    for i in digitos:
        if i == char:
            return entero
        entero += 1
    return 0


valores_extraidos = 0
mensaje_final = ""

def procesar_numero(numero, base_in, base_out):
    global msg_final
    global valores_extraidos
    global acumulador

    decimal = 0
    potencia = 0
    for i in range(len(numero)-1, -1, -1):
        conversor_entero = transformar_letra_entero(numero[i])
        valor_decimal += digito_entero * (base_in ** exponente)
        exponente += 1 # Se mueve la posicion a la izquierda en el numero

    if 32 <= valor_decimal <= 126:
        valores_extraidos += 1
    else:
        return




print("--- DECODIFICADOR DE NOTAS ---")


acumulador = ""
base_actual = None

while True:
    base_objetivo = int(input("Ingrese la base en la que desea visualizar los datos (2, 8, 10, 16): "))
    if base_objetivo not in [2, 8, 10, 16]:
        print("Por favor introduzca una base válida")
    else: break

print("[+] Procesando archivo: notas_dm.txt...")
print("[-] Filtrando ruido místico (valores fuera de rango ASCII)...")

print(f"LISTA DE VALORES EXTRAÍDOS (Base {base_objetivo}):")
print("--------------------------------------------------")

with open("notas_dm.txt", "r") as arch:
    while True:
        caracter = arch.read(1)
        if not caracter: #Fin del archivo
            if acumulador: #Por si habia un numero acumulado antes de terminar el archivo
                procesar_numero(acumulador, base_actual, base_objetivo)
            break 

        # 1- Es prefijo?
        if caracter in ["*", "&", "#", "!"]:
            if acumulador:
                # Check y procesamiento por si ya se venia armando un numero
                procesar_numero(acumulador, base_actual, base_objetivo)

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
                procesar_numero(acumulador, base_actual, base_objetivo)
                acumulador = ""
                base_actual = None 


        