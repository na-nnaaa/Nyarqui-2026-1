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


    OJOOOOOO FALTA LA TRANSFORMACION HEXADECIMAL A OCTAL AHI TE EXPLICO PQ
    USA EL ARCHIVO COSO PARA DEBUGEAR IKEROVICH BESITOS
    '''


def string_a_int(numero): #transforma un string a int, basicamente lo mismo que int() de python
    largo = len(numero) - 1
    numero_int = 0
    for digito in numero:
        if digito == "1":
            numero_int += (1 * (10**largo))
        elif digito == "2":
            numero_int += (2 * (10**largo))
        elif digito == "3":
            numero_int += (3 * (10**largo))
        elif digito == "4":
            numero_int += (4 * (10**largo))
        elif digito == "5":
            numero_int += (5 * (10**largo))
        elif digito == "6":
            numero_int += (6 * (10**largo))
        elif digito == "7":
            numero_int += (7 * (10**largo))
        elif digito == "8":
            numero_int += (8 * (10**largo))
        elif digito == "9":
            numero_int += (9 * (10**largo))
        
        largo -= 1
    return numero_int

def binario_a_decimal(numero): #recibe string pero retorna int (ver que conviene mas)
    largo = len(numero) - 1
    decimal = 0
    for digito in numero:
        if digito == "1":
            decimal += 1 * (2**largo)
        largo -= 1
    return str(decimal)

def binario_a_octal(numero): #recib string retornaa stringggggg
    octal = ""
    for i in range(len(numero), 0 , -3):
        inicio = i - 3 
        if inicio < 0 : inicio = 0

        digitos = numero[inicio:i]

        if digitos == "000" : octal += "0"
        elif digitos == "001" : octal += "1"
        elif digitos == "010" : octal += "2"
        elif digitos == "011" : octal += "3"
        elif digitos == "100" : octal += "4"
        elif digitos == "101" : octal += "5"
        elif digitos == "110" : octal += "6"
        elif digitos == "111" : octal += "7"

        elif digitos == "00" : octal += "0"
        elif digitos == "01" : octal += "1"
        elif digitos == "10" : octal += "2"
        elif digitos == "11" : octal += "3"

        elif digitos == "0" : octal += "0"
        elif digitos == "1" : octal += "1"

    return octal[::-1]
    
def binario_a_hexadecimal(numero): #recibe string y retorna string se asume igual que el numero es si o si uno valido
    hexadecimal = ""
    for i in range(len(numero), 0, -4):
        inicio = i - 4
        if inicio < 0: inicio = 0
        
        digitos = numero[inicio:i]

        if digitos == "0000" : hexadecimal += "0"
        elif digitos == "0001" : hexadecimal += "1"
        elif digitos == "0010" : hexadecimal += "2"
        elif digitos == "0011" : hexadecimal += "3"
        elif digitos == "0100" : hexadecimal += "4"
        elif digitos == "0101" : hexadecimal += "5"
        elif digitos == "0110" : hexadecimal += "6"
        elif digitos == "0111" : hexadecimal += "7"
        elif digitos == "1000" : hexadecimal += "8"
        elif digitos == "1001" : hexadecimal += "9"
        elif digitos == "1010" : hexadecimal += "A"
        elif digitos == "1011" : hexadecimal += "B"
        elif digitos == "1100" : hexadecimal += "C"
        elif digitos == "1101" : hexadecimal += "D"
        elif digitos == "1110" : hexadecimal += "E"
        elif digitos == "1111" : hexadecimal += "F"

        #si el conjunto de digitos es de largo 3
        elif digitos == "000" : hexadecimal += "0"
        elif digitos == "001" : hexadecimal += "1"
        elif digitos == "010" : hexadecimal += "2"
        elif digitos == "011" : hexadecimal += "3"
        elif digitos == "100" : hexadecimal += "4"
        elif digitos == "101" : hexadecimal += "5"
        elif digitos == "110" : hexadecimal += "6"
        elif digitos == "111" : hexadecimal += "7"

        #si el conjunto de digitos es de largo 2
        elif digitos == "00" : hexadecimal += "0"
        elif digitos == "01" : hexadecimal += "1"
        elif digitos == "10" : hexadecimal += "2"
        elif digitos == "11" : hexadecimal += "3"

        #si es de largo 1
        elif digitos == "0" : hexadecimal += "0"
        elif digitos == "1" : hexadecimal += "1"

    hexadecimal = hexadecimal[::-1] #damos vuelta la palabra para que quede bien el numero
    return hexadecimal

def decimal_a_binario(numero): #recibe string retorna string
    continuar = True
    numero_int = string_a_int(numero)
    binario =""

    while continuar:
        if numero_int % 2 == 0: binario += "0"
        else: binario += "1"
        numero_int = numero_int // 2
        if numero_int == 0: continuar = False
    return binario[::-1]

def decimal_a_octal(numero): #recibe string retorna string
    numero_int = string_a_int(numero)
    octal = ""
    resto = 0

    while True:
        resto = numero_int % 8
        if resto == 0 : octal += "0"
        elif resto == 1 : octal += "1"
        elif resto == 2 : octal += "2"
        elif resto == 3 : octal += "3"
        elif resto == 4 : octal += "4"
        elif resto == 5 : octal += "5"
        elif resto == 6 : octal += "6"
        elif resto == 7 : octal += "7"

        numero_int = numero_int // 8
        if numero_int == 0 : break
    return octal[::-1]

def decimal_a_hexadecimal(numero):#recibe string retor string
    numero_int = string_a_int(numero)
    resto = 0
    hexadecimal = ""
    while True:
        resto = numero_int % 16
        if resto == 0 : hexadecimal += "0"
        elif resto == 1 : hexadecimal += "1"
        elif resto == 2 : hexadecimal += "2"
        elif resto == 3 : hexadecimal += "3"
        elif resto == 4 : hexadecimal += "4"
        elif resto == 5 : hexadecimal += "5"
        elif resto == 6 : hexadecimal += "6"
        elif resto == 7 : hexadecimal += "7"
        elif resto == 8 : hexadecimal += "8"
        elif resto == 9 : hexadecimal += "9"
        elif resto == 10 : hexadecimal += "A"
        elif resto == 11 : hexadecimal += "B"
        elif resto == 12 : hexadecimal += "C"
        elif resto == 13 : hexadecimal += "D"
        elif resto == 14 : hexadecimal += "E"
        elif resto == 15 : hexadecimal += "F"
        numero_int = numero_int // 16
        
        if numero_int == 0 : break
    return hexadecimal[::-1]

def hexadecimal_a_binario(numero):# retorna y recibe string
    binario = ""
    for digito in numero:
        if digito == "0" : binario += "0000"
        elif digito == "1" : binario += "0001"
        elif digito == "2" : binario += "0010"
        elif digito == "3" : binario += "0011"
        elif digito == "4" : binario += "0100"
        elif digito == "5" : binario += "0101"
        elif digito == "6" : binario += "0110"
        elif digito == "7" : binario += "0111"
        elif digito == "8" : binario += "1000"
        elif digito == "9" : binario += "1001"
        elif digito == "A" : binario += "1010"
        elif digito == "B" : binario += "1011"
        elif digito == "C" : binario += "1100"
        elif digito == "D" : binario += "1101"
        elif digito == "E" : binario += "1110"
        elif digito == "F" : binario += "1111"
    
    return binario

def hexadecimal_a_decimal(numero): #string strins fskjfsflkjahsfñlkjashf
    largo = len(numero) - 1
    decimal = 0
    for digito in numero:
        if digito == "1":
            decimal += (1 * (16**largo))
        elif digito == "2":
            decimal += (2 * (16**largo))
        elif digito == "3":
            decimal += (3 * (16**largo))
        elif digito == "4":
            decimal += (4 * (16**largo))
        elif digito == "5":
            decimal += (5 * (16**largo))
        elif digito == "6":
            decimal += (6 * (16**largo))
        elif digito == "7":
            decimal += (7 * (16**largo))
        elif digito == "8":
            decimal += (8 * (16**largo))
        elif digito == "9":
            decimal += (9 * (16**largo))
        elif digito == "A":
            decimal += (10 * (16**largo))
        elif digito == "B":
            decimal += (11 * (16**largo))
        elif digito == "C":
            decimal += (12 * (16**largo))
        elif digito == "D":
            decimal += (13 * (16**largo))
        elif digito == "E":
            decimal += (14 * (16**largo))
        elif digito == "F":
            decimal += (15 * (16**largo))
        
        largo -= 1
    return str(decimal)



def es_digito_valido (digito, base): 
    if base == 2 and digito in "01": return True
    elif base == 8 and digito in "01234567": return True
    elif base == 10 and digito in "0123456789": return True
    elif base == 16 and digito in "0123456789ABCDEF": return True
    return 0

def transformar_letra_entero (char): #hexadecimal a decimal
    digitos = "0123456789ABCDEF"
    entero = 0
    for i in digitos:
        if i == char:
            return entero
        entero += 1
    return 0 #si no se encuentra en digitos retorna 0


valores_extraidos = 0
mensaje_final = ""

def procesar_numero(numero, base_in, base_out):
    global msg_final
    global valores_extraidos
    global acumulador

    decimal = 0
    potencia = 0
    for i in range(len(numero)-1, -1, -1):
        digito_entero = transformar_letra_entero(numero[i])
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
        caracter = arch.read(1) #captura un caracter
        if not caracter: #Fin del archivo
            if acumulador: #Por si habia un numero acumulado antes de terminar el archivo
                procesar_numero(acumulador, base_actual, base_objetivo)
            break 

        # 1- Es prefijo?
        if caracter in ["*", "&", "#", "!"]:
            if acumulador:
                # Check y procesamiento por si ya se venia armando un numero
                #
                # procesar_numero(acumulador, base_actual, base_objetivo)
                print(acumulador)
            if caracter == "*": base_actual = 2
            elif caracter == "&": base_actual = 8
            elif caracter == "#": base_actual = 10
            elif caracter == "!": base_actual = 16

            acumulador = "" #Se limpia para acumular el nuevo numero
        
        # 2- Es digito valido para la base?
        elif es_digito_valido(caracter, base_actual):
            acumulador += caracter
            print(acumulador)

        # 3- Es basura? (asumiendo que un numero invalido para la base tmb es basura)
        else: 
            if acumulador:
                #procesar_numero(acumulador, base_actual, base_objetivo)
                print(acumulador)
                acumulador = ""
                base_actual = None 


        