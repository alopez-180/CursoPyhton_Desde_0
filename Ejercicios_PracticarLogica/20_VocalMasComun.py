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
    vocales_pequeñas = []
    for i in vocales:
        for j in vocales:
            if (string.count(i) > string.count(j)): 
                if vocales_pequeñas.count(j) == 0:  # Añadimos a una lista, las vocales que menos aparecen ya que al hacer la comparación de i y j, las grandes nunca apareceran como j
                    vocales_pequeñas.append(j)

    for i in vocales_pequeñas:
        vocales.remove(i)
    
    contador = string.count(vocales[0])            
    if (len(vocales) > 1):
        print(f"Hay {len(vocales)} vocales que aparecen las mismas veces, un total de {contador}")
        print(f"{vocales}")
    else:
        print(f"La vocal {vocales} , es la que más aparece, con un total de {contador} veces.")

    
 
    
string = "Hola me llamo Pedriii"
countvocales(string)
