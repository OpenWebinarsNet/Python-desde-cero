# Función ConvertirABinario: Recibe un número entero y devuelve una cadena de
# caracteres con la representación binaria del número.
# Parámetros de entrada: Número entero a convertir
# Dato devuelto: Cadena de caracteres con el número binario

def ConvertirABinario(decimal):
    binario = ""
    # Realizo divisiones sucesivas entre 2 guardando el resto (1 o 0)
    while decimal>1:
        # Concatenamos en orden inverso los restos de la división entre 2.
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    binario = str(decimal) + binario
    return binario

# Función ConvertirADecimal: Recibe una cadena de caracteres con la representación
#  de un número binario y devuelve el entero correspondiente.
# Parámetros de entrada: Cadena de caracteres con el número binario
# Dato devuelto: Entero

def ConvertirADecimal(binario):
    decimal = 0
    exponente = 1
    # Voy acumulando el valor de la cifra binario elevado a un exponente que
    #depende de su posición.
    # La última cifra hay que elevar al exponete 1, la siguiente 2, la siguiente
    # 4, y así sucesivamente.
    for caracter in binario[::-1]:
        if caracter == "1":
            decimal = decimal + exponente
		# El exponente se va doblando en cada iteración
        exponente = exponente * 2
    return decimal

# Función EsBinario: Recibe una cadena de caracteres con la representación
#  de un número binario y devuelve un valor lógico indicando si realmente es un
# número binario (Tienes 1 y 0) verdadero, y falso en caso contrario.
# Parámetros de entrada: Cadena de caracteres con el número binario
# Dato devuelto: Valor lógico

def EsBinario(binario):
    for caracter in binario:
        if caracter not in ["1","0"]:
            return False
    return True

# Crea un programa principal que permita convertir de decimal a binario y de
# binario a decimal.

decimal = int(input("Dime un número decimal:"))
print("Número binario:",ConvertirABinario(decimal))
while True:
    binario = input("Dime un número en binario:")
    if EsBinario(binario):
        break
print("Número decimal:",ConvertirADecimal(binario))
