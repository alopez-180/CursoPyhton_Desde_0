"""
/*
 * Escribe una función que calcule si un número dado es un número de Armstrong
 * (o también llamado narcisista).
 * Si no conoces qué es un número de Armstrong, debes buscar información
 * al respecto.
 */
"""
#Un número Armstrong es aquel que cumple la siguiente propiedad: la suma 
# de las potencias n-ésimas de sus dígitos es igual al propio número. 
# Por ejemplo, el número 153 es un número Armstrong, ya que 1^3 + 5^3 + 3^3 = 153.

def calcular_num_armstrong (numero):
    resultado = 0
    for i in str(numero):
        integer = int(i)
        suma = (integer ** (len(str(numero))))
        resultado = resultado + suma
    if (resultado == numero):
        print(f"El numero {numero} es un numero de Armstrong")
    else:
        print(f"El numero {numero} no es un numero de Armstrong")


numero = int(input("Escribe el número que quieres calcular si es Armstrong o no: "))
calcular_num_armstrong(numero)

