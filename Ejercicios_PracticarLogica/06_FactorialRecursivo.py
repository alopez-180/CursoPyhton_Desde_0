"""
/*
 * Escribe una función que calcule y retorne el factorial de un número dado
 * de forma recursiva.
 */
"""

def calcular_factorial(numero):
    factorial = 1
    rango = []
    if numero == 0:
        factorial = 1
    else: 
        for i in range (1, numero+1):
            factorial = factorial * i
            rango.append(str(i))
    rango = (" + ".join(rango))
    return numero, factorial, rango
 

numero = int(input("Escribe el número del que quieres calcular el factorial: "))
factorial = calcular_factorial(numero)
print(f" {factorial[0]}! = {factorial[2]} = {factorial[1]}")
