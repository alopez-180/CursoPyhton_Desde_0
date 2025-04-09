"""
/*
 * Crea 3 funciones, cada una encargada de detectar si una cadena de
 * texto es un heterograma, un isograma o un pangrama.
 * - Debes buscar la definición de cada uno de estos términos.
 */

Heterograma: Es una palabra o frase en la que no se repite ninguna letra. Por ejemplo, "murciélago" es un heterograma porque cada letra aparece solo una vez.

Isograma: Es una palabra o frase en la que cada letra aparece el mismo número de veces. Por ejemplo, "deed" (en inglés) es un isograma porque cada letra aparece dos veces.

Panagrama: Es una frase que contiene todas las letras del alfabeto al menos una vez. Un ejemplo famoso en inglés es "The quick brown fox jumps over the lazy dog".

"""

def heterograma(str1):
    letras_repetidas = []
    for i in str1:
        if str1.count(i) > 1:
            letras_repetidas.append(i)
        
    es_heterograma = len(letras_repetidas)
    if es_heterograma > 0:
        print("La cadena no es heterograma")
    else:
        print("La cadena es heterograma")


def isograma (str1):
    str1 = str1.lower()
    cadena = []
    diccionario = {}

    for i in str1:
        cadena.append(i)
    diccionario = dict.fromkeys(cadena)

    for i in str1:
        val = str1.count(i)
        diccionario[i] = val

    cadena = []

    for i in diccionario:
        val = diccionario[i]
        cadena.append(val)

    valor = 0
    for i in cadena:
        for j in cadena:
            if (i != j):
                valor += 1
    
    if (valor > 1):
        print("La cadena no es isometrica")
    else:
        print("La cadena es isometrica")


def panagrana (str1):
    str1 = str1.replace(" ","")
    
    abecedario = []
    str1 = str1.upper()
    for i in range (65,91):
        abecedario.append(chr(i))

    array = []
    
    for i in str1:
        array.append(i)

    array_copia = array
    
    for i in array_copia:
        if array.count(i) > 1:
            for j in range(array.count(i)-1):
                array.remove(i)
        
    for i in array:
        abecedario.remove(i)
    
    if len(abecedario) != 0:
        print("El string no es un panagrama")
    else:
        print("El strign sí es un panagrama")



str1 = "The quick brown fox jumps over the lazy doog"
heterograma(str1)
isograma(str1)
panagrana(str1)

