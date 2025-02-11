"""
/*
 * Crea un programa que dibuje un cuadrado o un triángulo con asteriscos "*".
 * - Indicaremos el tamaño del lado y si la figura a dibujar es una u otra.
 * - EXTRA: ¿Eres capaz de dibujar más figuras?
 */
"""

tamaño = 5

for vertical in range (tamaño):
    for horizontal in range (tamaño):
        if (vertical == 0 or vertical == tamaño-1 or (horizontal == 0 or horizontal == tamaño-1)):
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print(" ")

print("############")

for horizontal in range (tamaño):
    for vertical in range (tamaño):
        print("*", end=" ")
    print(" ")

print("############")

for i in range(tamaño):
    for j in range(i+1):
        print("*",end=" ")
    print(" ")

print("############")

for i in range(tamaño+1,0,-1):
    for j in range(i-1):
        print("*",end=" ")
    print(" ")

print("############")
