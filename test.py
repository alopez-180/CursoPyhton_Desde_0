"""
 * Crea un programa se encargue de transformar un número
 * decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
"""
sigue = True

while sigue:
    try:
        numero = int(input("Escribe un numero en decimal: "))
        sigue = False
    except ValueError:
        print("Error, introduce un numero decimal: ")


sigue = True
numeros_binario = []
division = numero

while sigue: 
    if division > 0:
        resto = division % 2  
        numeros_binario.append(int(resto))
        division = division // 2
        division = int(division)
    elif division == 0:
        sigue = False

ordenar_numeros = []
for i in (numeros_binario[::-1]):
    ordenar_numeros.append(i) 
       
print(ordenar_numeros)
