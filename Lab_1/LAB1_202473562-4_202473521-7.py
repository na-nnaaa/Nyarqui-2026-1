def string_a_int(numero): #transforma un string a int, basicamente lo mismo que int() de python

    """
    Convierte un string numérico a su valor entero (int).
    Se basa en multiplicar cada 
    dígito por 10 elevado a su posición (sistema decimal posicional).
    """
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

    """
    Convierte un string que representa un número binario a un string decimal.
    Itera sobre el string multiplicando los '1' por 2 elevado a la 
    posición correspondiente.
    """
    largo = len(numero) - 1
    decimal = 0
    for digito in numero:
        if digito == "1":
            decimal += 1 * (2**largo)
        largo -= 1
    return str(decimal)

def binario_a_octal(numero): #recib string retornaa stringggggg

    """
    Convierte un string binario directamente a octal agrupando los bits de a 3,
    leyendo de derecha a izquierda.
    """
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

    """
    Convierte un string binario a hexadecimal agrupando los bits de a 4.
    Implementado mediante evaluación exhaustiva (hardcodeadaxd) de cada bloque posible,
    asegurando la conversión manual pura requerida.
    """    
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


def octal_a_decimal (numero):

    """
    Convierte un string octal a string decimal.
    Usa el sistema posicional donde cada dígito se multiplica por 
    8 elevado a su posición.
    """
    largo = len(numero) - 1
    decimal = 0
    for digito in numero:
        valor = transformar_letra_entero(digito)
        decimal += valor * (8**largo)
        largo -= 1
    return str(decimal)

def octal_a_binario(numero):
    """
    Transformación directa de octal a binario reemplazando cada dígito
    por su equivalente estricto de 3 bits.
    """
    binario = ""
    for digito in numero:
        if digito == "0": binario += "000"
        elif digito == "1": binario += "001"
        elif digito == "2": binario += "010"
        elif digito == "3": binario += "011"
        elif digito == "4": binario += "100"
        elif digito == "5": binario += "101"
        elif digito == "6": binario += "110"
        elif digito == "7": binario += "111"
    
    # Quita los ceros iniciales del primer bloque para que quede limpio
    while len(binario) > 1 and binario[0] == "0":
        binario = binario[1:]
        
    return binario

def octal_a_hexadecimal(numero):
    """
    Conversión directa de octal a hexadecimal. 
    Calcula el valor posicional (base 8) y aplica divisiones sucesivas 
    por 16
    """
    # 1. Calcular valor matemático posicional
    largo = len(numero) - 1
    valor = 0
    for digito in numero:
        if digito == "1": valor += 1 * (8**largo)
        elif digito == "2": valor += 2 * (8**largo)
        elif digito == "3": valor += 3 * (8**largo)
        elif digito == "4": valor += 4 * (8**largo)
        elif digito == "5": valor += 5 * (8**largo)
        elif digito == "6": valor += 6 * (8**largo)
        elif digito == "7": valor += 7 * (8**largo)
        largo -= 1
        
    if valor == 0: return "0"
        
    # 2. Divisiones sucesivas por 16 directas
    hexadecimal = ""
    while True:
        resto = valor % 16
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
        
        valor = valor // 16
        if valor == 0: break
        
    return hexadecimal[::-1]

def decimal_a_binario(numero): #recibe string retorna string

    """
    Convierte un string decimal a string binario utilizando el método
    matemático de divisiones sucesivas por 2, guardando los restos.
    """
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

    """
    Convierte un string decimal a string octal utilizando divisiones 
    sucesivas por 8 y rescatando los restos generados.
    """
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

    """
    Convierte un string decimal a un string hexadecimal mediante divisiones
    sucesivas por 16. Los restos mayores a 9 se asignan manualmente a su
    letra correspondiente (A-F).
    """
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

    """
    Convierte un string hexadecimal directamente a binario asignando
    a cada carácter su bloque equivalente de 4 bits.
    """
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

def hexadecimal_a_decimal(numero): 

    """
    Convierte un string hexadecimal a string decimal empleando evaluación 
    posicional (multiplicando por potencias de 16).
    """
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

def hexadecimal_a_octal(numero):
    """
    Conversión directa de hexadecimal a octal.
    Calcula el valor posicional (base 16) y aplica divisiones sucesivas 
    por 8 en un solo flujo algorítmico autónomo.
    """
    largo = len(numero) - 1
    valor = 0
    for digito in numero:
        if digito == "1": valor += 1 * (16**largo)
        elif digito == "2": valor += 2 * (16**largo)
        elif digito == "3": valor += 3 * (16**largo)
        elif digito == "4": valor += 4 * (16**largo)
        elif digito == "5": valor += 5 * (16**largo)
        elif digito == "6": valor += 6 * (16**largo)
        elif digito == "7": valor += 7 * (16**largo)
        elif digito == "8": valor += 8 * (16**largo)
        elif digito == "9": valor += 9 * (16**largo)
        elif digito == "A": valor += 10 * (16**largo)
        elif digito == "B": valor += 11 * (16**largo)
        elif digito == "C": valor += 12 * (16**largo)
        elif digito == "D": valor += 13 * (16**largo)
        elif digito == "E": valor += 14 * (16**largo)
        elif digito == "F": valor += 15 * (16**largo)
        largo -= 1
        
    if valor == 0: return "0"
        
    octal = ""
    while True:
        resto = valor % 8
        if resto == 0 : octal += "0"
        elif resto == 1 : octal += "1"
        elif resto == 2 : octal += "2"
        elif resto == 3 : octal += "3"
        elif resto == 4 : octal += "4"
        elif resto == 5 : octal += "5"
        elif resto == 6 : octal += "6"
        elif resto == 7 : octal += "7"
        
        valor = valor // 8
        if valor == 0: break
        
    return octal[::-1]

def es_digito_valido (digito, base): 
    """
    Verifica si un carácter es válido para la base actual.
    Esta función es el pilar de la regla para ignorar basura.
    Permite detectar cuándo un número ha terminado y cuándo comienza
    un carácter de "ruido" que debe interrumpir la captura de dígitos.
    """
    if base == 2 and digito in "01": return True
    elif base == 8 and digito in "01234567": return True
    elif base == 10 and digito in "0123456789": return True
    elif base == 16 and digito in "0123456789ABCDEF": return True
    return False

def transformar_letra_entero (char): #hexadecimal a decimal

    """
        Retorna el valor numérico base 10 de un caracter hexadecimal 
        (ej: 'A' -> 10, 'F' -> 15) para facilitar cálculos algebraicos.
    """
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
    """
    Centraliza toda la logica
    1. Calcula el valor decimal SOLO para la validación ASCII.
    2. Verifica que esté entre 32 y 126.
    3. Si es válido, lo transforma directamente de base_in a base_out (sin puente decimal).
    4. Imprime el resultado en pantalla y añade la letra al mensaje final ASCII.
    """
    global valores_extraidos
    global mensaje_final

    # Obtener el decimal para validación del rango ASCII
    if base_in == 2:
        val_decimal_str = binario_a_decimal(numero)
    elif base_in == 8:
        val_decimal_str = octal_a_decimal(numero)
    elif base_in == 10:
        val_decimal_str = numero
    elif base_in == 16:
        val_decimal_str = hexadecimal_a_decimal(numero)

    val_decimal_int = string_a_int(val_decimal_str)

    # Filtrado por rango (32 a 126)
    if 32 <= val_decimal_int <= 126:
        valores_extraidos += 1
        
        # CONVERSIÓN DIRECTA DE BASE A BASE
        if base_in == base_out:
            res_visual = numero
            
        elif base_in == 2:
            if base_out == 8: res_visual = binario_a_octal(numero)
            elif base_out == 10: res_visual = binario_a_decimal(numero)
            elif base_out == 16: res_visual = binario_a_hexadecimal(numero)
            
        elif base_in == 8:
            if base_out == 2: res_visual = octal_a_binario(numero)
            elif base_out == 10: res_visual = octal_a_decimal(numero)
            elif base_out == 16: res_visual = octal_a_hexadecimal(numero)
            
        elif base_in == 10:
            if base_out == 2: res_visual = decimal_a_binario(numero)
            elif base_out == 8: res_visual = decimal_a_octal(numero)
            elif base_out == 16: res_visual = decimal_a_hexadecimal(numero)
            
        elif base_in == 16:
            if base_out == 2: res_visual = hexadecimal_a_binario(numero)
            elif base_out == 8: res_visual = hexadecimal_a_octal(numero)
            elif base_out == 10: res_visual = hexadecimal_a_decimal(numero)

        # Print salida
        nombres = {2: "Binario", 8: "Octal", 10: "Decimal", 16: "Hexadecimal"}
        simbolos = {2: "*", 8: "&", 10: "#", 16: "!"}

        print(f"Valor {valores_extraidos}: {res_visual} (Original: {nombres[base_in]} {simbolos[base_in]}{numero})")

        mensaje_final += chr(val_decimal_int)


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
try:
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

except FileNotFoundError:
    print("[-] ERROR CRÍTICO: No se pudo encontrar el archivo 'notas_dm.txt'.")
    print("[-] Asegúrate de que el archivo exista en la misma carpeta que este programa.")
    print("[!] Abortando misión...")
except Exception as e:
    print(f"\n[-] ERROR CRÍTICO: Ocurrió un error inesperado al leer el archivo: {e}")
    print("[!] Abortando misión...")

print("--------------------------------------------------")

if mensaje_final:
    print(f"\nMENSAJE DECODIFICADO:\n\"{mensaje_final}\"")

        