"""
/*
 * Crea una función que reciba dos array, un booleano y retorne un array.
 * - Si el booleano es verdadero buscará y retornará los elementos comunes
 *   de los dos array.
 * - Si el booleano es falso buscará y retornará los elementos no comunes
 *   de los dos array.
 * - No se pueden utilizar operaciones del lenguaje que
 *   lo resuelvan directamente.
 */
"""

def funcion(array1, array2, bool):
    resultado = []
    
    if(bool == True):
        for i in array1:
            for j in array2:
                if i == j and (resultado.count(i) == 0):
                    resultado.append(i)
        return resultado
    
    elif(bool == False):
        for i in array1:
            contar = array2.count(i)
            if (contar == 0):
                resultado.append(i)
        for j in array2:
            contar = array1.count(j)
            if (contar == 0):
                resultado.append(j)  
        return resultado
    else:
        print("Error")


array1 = ["Hola", 2, "que", 5, "Tal?"]
array2 = ["Hola", 2, "Que", 1, "Tal?"]
bool = False
resultado = funcion(array1, array2, bool)
print(resultado)