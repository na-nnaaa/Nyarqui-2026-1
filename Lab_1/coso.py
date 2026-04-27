def transformar_letra_entero (char):
    digitos = "0123456789ABCDEF"
    entero = 0
    for i in digitos:
        if i == char:
            return entero
        entero += 1
    return 0




def binario_a_decimal(numero):
    largo = len(numero) - 1
    decimal = 0
    for digito in numero:
        if digito == "1":
            decimal += 1 * (2**largo)
        largo -= 1
    return decimal 
#print(binario_a_decimal("10110"))

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

print(binario_a_hexadecimal("11110101010"))
def string_a_int(numero): #transforma un numero como 10010 de texto a numero
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

def decimal_a_binario(numero):
    continuar = True
    numero_int = string_a_int(numero)
    binario =""

    while continuar:
        if numero_int % 2 == 0: binario += "0"
        else: binario += "1"
        numero_int = numero_int // 2
        if numero_int == 0: continuar = False
    return binario[::-1]

print(decimal_a_binario("16"))
      
def decimal_a_hexadecimal(numero):
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


print(string_a_int("16"))
print(decimal_a_hexadecimal("255"))

def binario_a_octal(numero):
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

print(binario_a_octal("110011"))

def decimal_a_octal(numero):
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
print(decimal_a_octal("12340"))

def hexadecimal_a_binario(numero):
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
print(hexadecimal_a_binario("F10A"))

def hexadecimal_a_decimal(numero):
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
print(hexadecimal_a_decimal("14"))