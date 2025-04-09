"""
/*
 * Crea una función que sea capaz de detectar y retornar todos los
 * handles de un texto usando solamente Expresiones Regulares.
 * Debes crear una expresión regular para cada caso:
 * - Handle usuario: Los que comienzan por "@"
 * - Handle hashtag: Los que comienzan por "#"
 * - Handle web: Los que comienzan por "www.", "http://", "https://"
 *   y finalizan con un dominio (.com, .es...)
 */
"""

def handles (str1):
    str1 = str1 + " "
    array = []
    cadena = ""
    for i in str1:
        if i == " ":
            array.append(cadena)
            cadena = ""
        else:
            cadena = cadena + i

    handles = []
    for i in array:
        if i[0:1] == "#":
            handles.append(i)
        elif i[0:1] == "@":
            handles.append(i)  
        elif i[0:4] == "www.":
            handles.append(i)  
        elif i[0:7] == "https://" and i [-3:] == ".es" or i [-4:] == ".com":
            handles.append(i)   
        elif i[0:7] == "http://" and i [-3:] == ".es" or i [-4:] == ".com":
            handles.append(i)

    return handles

str1 = "@Hola #que http://tal.es como estas"
print(handles(str1))
 