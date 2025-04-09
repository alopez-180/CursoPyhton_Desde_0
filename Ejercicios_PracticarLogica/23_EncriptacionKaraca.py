"""
/*
 * Crea una función que sea capaz de encriptar y desencriptar texto
 * utilizando el algoritmo de encriptación de Karaca
 * (debes buscar información sobre él).
 */

 1. Invertir Texto
 2. Remplazar las vocales por numeros:
    
    a => 0
    e => 1
    i => 2
    o => 3
    u => 4
 3. Añadir aca al final    
 """



################################################
# Encriptador 1 - no es poden ficar numeros perque els encripta com si fosin vocals                                              #
################################################
"""
def encriptator (str1):
    cadena = ""
    str1 = str1.lower()
    
    alreves = ""
    for i in str1:
        alreves = i + alreves

    for i in alreves:
        if i == "a":
            i = "0"
            cadena = cadena + i
        elif i == "e":
            i = "1"
            cadena = cadena + i
        elif i == "i":
            i = "2"
            cadena = cadena + i
        elif i == "o":
            i = "3"
            cadena = cadena + i
        elif i == "u":
            i = "4"
            cadena = cadena + i
        else:
            cadena = cadena + i

        cadena_encriptada = cadena + "aca"

    return cadena_encriptada

    
"""

################################################
# Desencripador                                #
################################################

def desencriptator(cadena_encriptada):
    cadena = ""
    for i in cadena_encriptada:
        cadena = i + cadena

    cadena = cadena[3:]
    cadena_desencriptada = ""
    for i in cadena: 
        if i == "0":
            i = "a"
            cadena_desencriptada = cadena_desencriptada + i
        elif i == "1":
            i = "e"
            cadena_desencriptada = cadena_desencriptada + i
        elif i == "2":
            i = "i"
            cadena_desencriptada = cadena_desencriptada + i
        elif i == "3":
            i = "o"
            cadena_desencriptada = cadena_desencriptada + i
        elif i == "4":
            i = "u"
            cadena_desencriptada = cadena_desencriptada + i
        elif i == "·":
            i = "0"
            cadena_desencriptada = cadena_desencriptada + i
        elif i == "ª":
            i = "1"
            cadena_desencriptada = cadena_desencriptada + i
        elif i == "º":
            i = "2"
            cadena_desencriptada = cadena_desencriptada + i
        elif i == "|":
            i = "3"
            cadena_desencriptada = cadena_desencriptada + i
        elif i == "¬":
            i = "4"
            cadena_desencriptada = cadena_desencriptada + i
        
        else:
            cadena_desencriptada = cadena_desencriptada + i

    return cadena_desencriptada

""""
str1 = str(input("Introduce un texto ha cifrar: "))
cadena_encriptada = encriptator(str1)

print(cadena_encriptada)

cadena_desencriptada = desencriptator(cadena_encriptada)
print(cadena_desencriptada)

"""

################################################
# Encriptador 2 - es poden ficar numeros       #
################################################

def encriptator2(str1):
    alreves = ""
    for i in str1:
        alreves = i + alreves
    
    cadenall = ""
    
    for i in alreves:
        if i == "0":
            i = "·"
            cadenall = cadenall + i
        elif i == "1":
            i = "ª"
            cadenall = cadenall + i  
        elif i == "2": 
            i = "º"
            cadenall = cadenall + i
        elif i == "3":
            i = "|"
            cadenall = cadenall + i
        elif i == "4":
            i = "¬" 
            cadenall = cadenall + i 
        else:
            cadenall = cadenall + i
            
    cadena2 = ""

    for i in cadenall:
        if i == "a":
            i = "0"
            cadena2 = cadena2 + i
        elif i == "e":
            i = "1"
            cadena2 = cadena2 + i
        elif i == "i": 
            i = "2"
            cadena2 = cadena2 + i
        elif i == "o":
            i = "3"
            cadena2 = cadena2 + i
        elif i == "u":
            i = "4" 
            cadena2 = cadena2 + i
        else:
            cadena2 = cadena2 + i

    cadena2 = cadena2 + "aca"
    return cadena2

str1 = "0Hola como estas"
a = (encriptator2(str1))
print(desencriptator(a))