"""
/*
 * Crea una función que transforme grados Celsius en Fahrenheit
 * y viceversa.
 *
 * - Para que un dato de entrada sea correcto debe poseer un símbolo "°"
 *   y su unidad ("C" o "F").
 * - En caso contrario retornará un error.
 */
"""

def transformar(grados, tipo):
    if (tipo == "grados"):
        # F = (C * 1,8) + 32
        temperatura = ((grados * 1.8) + 32)
        tipo = "F"

    elif (tipo == "fahrenheit"):
        # C = (F - 32) / 1,8
        temperatura = ((grados - 32) / 1.8)
        tipo = "C"

    return tipo, temperatura    

grados = 30
tipo = "grados"
resultado = transformar(grados, tipo)

print(f"La conversion de {grados} {tipo} a {resultado[0]} es = {resultado[1]} {resultado[0]}")