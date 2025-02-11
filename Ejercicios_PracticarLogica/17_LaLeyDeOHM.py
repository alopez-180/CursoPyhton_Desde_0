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

def ley_ohm (I=0, R=0, V=0):

    if I == 0:
        resultado = (V / R)

    elif V == 0:
        resultado = (I * R)

    elif R == 0:
        resultado = (V / I)

    else:
        resultado = "Error"

    return(resultado)


I = 5
V = 12
R = 0
resultado = ley_ohm(I, V)
print(resultado)