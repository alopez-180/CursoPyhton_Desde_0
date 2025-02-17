"""
/*
 * Crea un función que reciba un texto y retorne la vocal que
 * más veces se repita.
 * - Ten cuidado con algunos casos especiales.
 * - Si no hay vocales podrá devolver vacío.
 */
"""

def countvocales (string):
    string = string.lower()
    vocales = ["a", "e", "i", "o", "u"]
    masvocales = []

    for i in vocales:
        count_i = (string.count(i))
        for j in vocales:
            count_j = (string.count(j))
            if (count_i > count_j):
                if masvocales.count(i) == 0:
                    masvocales.append(i)
                vocales.remove(j)
    
    if (len(masvocales) > 1):
        veces = ' '.join(masvocales)
        veces = string.count(veces[0])
        return (f"Hay dos vocales que aparecen las mismas veces: {masvocales}, en un total de {veces} veces")

    else:
        letra = ' '.join(masvocales)
        veces = string.count(letra)
        return (f"La vocal que aparece más veces es la: {letra}, con un total de {veces} veces ")

    
string = "Hola me llamo Pedro ooaa aa"
resultado = countvocales(string)
print(resultado)