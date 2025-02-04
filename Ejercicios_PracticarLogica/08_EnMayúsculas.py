"""
/*
 * Crea una función que reciba un String de cualquier tipo y se encargue de
 * poner en mayúscula la primera letra de cada palabra.
 * - No se pueden utilizar operaciones del lenguaje que
 *   lo resuelvan directamente.
 */
"""

def mayusculas():
    frase = str(input("Introduce una frase: "))
    frase = (frase + " ")
    palabras = []
    palabra = ""

    for i in (frase):
        if (i != " "):
            palabra = palabra + i
        else:
            palabras.append(palabra)
            palabra = ""
    
    for i in palabras:
        letra = i[0]
        if (ord(letra) >= 97 and ord(letra) <=122) :
            lower = ord(letra)
            lower = (lower - 32)
            upper = chr(lower)
            palabra = upper + i[1:]
            index = palabras.index(i)
            palabras.pop(index)
            palabras.insert(index, palabra)
        
        else:
            print("Nada")

    return palabras

resultado = mayusculas()
resultado = ' '.join(resultado)
print(resultado)