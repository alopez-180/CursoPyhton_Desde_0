"""
/*
 * Crea un programa se encargue de transformar un número
 * decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
 */
 """

# https://www.binarydecode.com/es/decimal-to-binary-conversion

numero_decimal = float(input("Introduce el número que deseas convertir a binario: "))
numero_inicial = numero_decimal
numeros_binarios = []
continuar = True

while continuar:
    if numero_decimal >=1: 
        resto = numero_decimal % 2
        numeros_binarios.append(int(resto))
        numero_decimal = numero_decimal // 2
    else:
        continuar = False

print(numeros_binarios)


# Leer de final a inicio

numeros_ordenados = []
for i in numeros_binarios[::-1]:
    numeros_ordenados.append(i)

print(f"El numero {numero_inicial} convertido en binario es: {numeros_ordenados}")