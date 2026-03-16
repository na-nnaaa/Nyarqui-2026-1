
def string_a_int(numero): #transforma un string a int, basicamente lo mismo que int() de python
    largo = len(numero) - 1
    numero_int = 0
    for digito in numero:
        if digito == "0":
            numero_int += (0 * (10**largo))
        elif digito == "1":
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

def octal_a_decimal (numero):
    largo = len(numero) - 1
    decimal = 0
    for digito in numero:
        valor = transformar_letra_entero(digito)
        decimal += valor * (8**largo)
        largo -= 1
    return str(decimal)

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
    return False

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
    global mensaje_final
    global valores_extraidos

    if base_in == 2:
        val_decimal_str = binario_a_decimal(numero)
    elif base_in == 8:
        val_decimal_str = octal_a_decimal(numero)
    elif base_in == 10:
        val_decimal_str = numero
    elif base_in == 16:
        val_decimal_str = hexadecimal_a_decimal(numero)

    val_decimal_int = string_a_int(val_decimal_str)

    if 32 <= val_decimal_int <= 126:
        valores_extraidos += 1
    
        if base_out == 2:
            res_visual = decimal_a_binario(val_decimal_str)
        elif base_out == 8:
            res_visual = decimal_a_octal(val_decimal_str)
        elif base_out == 10:
            res_visual = val_decimal_str
        elif base_out == 16:
            res_visual = decimal_a_hexadecimal(val_decimal_str)

        nombres = {2: "Binario", 8: "Octal", 10: "Decimal", 16: "Hexadecimal"}
        simbolos = {2: "*", 8: "&", 10: "#", 16: "!"}

        print(f"Valor {valores_extraidos}: {res_visual} (Original: {nombres[base_in]} {simbolos[base_in]}{numero})")

        mensaje_final += chr(decimal_int)


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
        elif es_digito_valido(caracter, base_actual):
            acumulador += caracter

        # 3- Es basura? (asumiendo que un numero invalido para la base tmb es basura)
        else: 
            if acumulador:
                procesar_numero(acumulador, base_actual, base_objetivo)
                acumulador = ""
                base_actual = None 

print("--------------------------------------------------")
print(f"\nMENSAJE DECODIFICADO:\n\"{mensaje_final}\"")

        