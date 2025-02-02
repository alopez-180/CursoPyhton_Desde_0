"""
/*
 * Crea una función que reciba dos cadenas como parámetro (str1, str2)
 * e imprima otras dos cadenas como salida (out1, out2).
 * - out1 contendrá todos los caracteres presentes en la str1 pero NO
 *   estén presentes en str2.
 * - out2 contendrá todos los caracteres presentes en la str2 pero NO
 *   estén presentes en str1.
 */
"""

def cadenas (str1,str2):
    
    print(f"La primera cadena és: {str1}")
    print(f"La segunda cadena és: {str2}")

    str1 = str1.lower() # Ponemos todas las letras en minusculas 
    str2 = str2.lower() # Ponemos todas las letras en minusculas

    # Definimos variables    
    out1 = []
    out2 = []
    letras_iguales = []

    # Añadimos los str a un array
    for i in str1:
        out1.append(i)
    for i in str2:
        out2.append(i)
    
    # Comparamos las letras iguales que hay en los dos str
    for i in (str1):
        for j in (str2):
            if i == j:
                letras_iguales.append(i)

    # Cojemos las letras que no son las iguales del str1

    for i in letras_iguales:
        try:    
            index = out1.index(i)
            out1.pop(index)
        except ValueError:
            print("",end="")
    
            
    # Cojemos las letras que no son las iguales del str2        

    for i in letras_iguales:
        try:    
            index = out2.index(i)
            out2.pop(index)
        except ValueError:
            print("",end="")

    return out1, out2


out1, out2 = cadenas("aaab", "aaac")
# Imprimir los valores fuera de la función
print("out1:", out1)
print("out2:", out2)