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

# Pedimos al usuario las cadenas de caracteres
str1 = str(input("Introduce la cadena 1: "))
str2 = str(input("Introduce la cadena 2: "))

# Definimos variables como arrays
out1 = []
out2 = []
str1_array = []
str2_array = []

# Añadimos a los arrays cada uno de los caracteres que nos han pasado los usuarios en string
for i in str1:
    str1_array.append(i)

for i in str2:
    str2_array.append(i)

########################

coincidencias =[] # Definimos un nuevo array donde guardaremos las coincidencias de caracteres

for i in str1_array:  # Recorremos el array del primet str
    for j in str2_array: # Recorremos el array del segundo str
        if i == j and coincidencias.count(i) == 0:  # Si el caracter del primer str i del segundo coinciden y a parte no se ha añadido a las coincidencias todavia ningun caracter igual
            coincidencias.append(i) # Se le añade como coincidencia


# Una vez tenemos todas las coincidencias, hacemos lo siguiente: 
for i in str1_array: # recorremos el primer str
    for j in coincidencias: # recorremos el array con las coincidencias
        if i == j: # Si el caracter es una coincidencia
            a = str1_array.index(i) # Obtenemos su indice
            str1_array[a] = ""  # Y lo substituimos por un caracter vacio, ya que si lo borramos directamente alteraremos los indices y el for i in no lo ara bien           
                    
for i in str2_array:
    for j in coincidencias:
        if i == j:
            a = str2_array.index(i)
            str2_array[a] = ""            
                    

for i in str1_array: # cuando todos los caracteres que coinciden son subtituidos por "", solo quedan los valores buenos
    if i != "":
        out1.append(i)

for i in str2_array: 
    if i != "":
        out2.append(i)

print(f"final: {out1}")
print(f"final: {out2}")


        

