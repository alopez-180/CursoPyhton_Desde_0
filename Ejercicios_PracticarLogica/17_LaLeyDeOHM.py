"""
/*
 * Crea una función que calcule el valor del parámetro perdido
 * correspondiente a la ley de Ohm.
 * - Enviaremos a la función 2 de los 3 parámetros (V, R, I), y retornará
 *   el valor del tercero (redondeado a 2 decimales).
 * - Si los parámetros son incorrectos o insuficientes, la función retornará
 *   la cadena de texto "Invalid values".
 */
"""
# https://www.electrontools.com/Home/WP/ley-de-ohm-formula-y-ejemplos/
# la tensión (V), la corriente (I) y la resistencia (R) en un circuito eléctrico
# V = I * R
# I = V / R
# R = V / I

def ley_ohm (I=0, R=0, V=0):

    if I == 0:
        resultado = round((V / R), 2)
    elif V == 0:
        resultado = round((I * R), 2)
    elif R == 0:
        resultado = round((V / I), 2)
    else:
        resultado = "Invalid values"

    return(resultado)


I = 54
V = 12
R = 0
resultado = ley_ohm(I=I, V=V)
print(resultado)