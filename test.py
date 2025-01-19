"""
 * Crea un programa se encargue de transformar un número
 * decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
"""
sigue = True

while sigue:
    try:
        numero = float(input("Escribe un numero en decimal: "))
        sigue = False
    except ValueError:
        print("Error, introduce un numero decimal: ")


sigue = True
numeros_binario = []


division = numero // 2 
division = int(division)
resto = numero % 2 
numeros_binario.append(int(resto))

while sigue: 
    if division >> 0:
        division = division / 2
        division = int(division)
        print(division)
        resto = division % 2  
        numeros_binario.append(int(resto))

    elif division == 0:
        sigue = False

print(numeros_binario)
