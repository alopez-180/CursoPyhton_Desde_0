"""
/*
 * Crea una función que ordene y retorne una matriz de números.
 * - La función recibirá un listado (por ejemplo [2, 4, 6, 8, 9]) y un parámetro
 *   adicional "Asc" o "Desc" para indicar si debe ordenarse de menor a mayor
 *   o de mayor a menor.
 * - No se pueden utilizar funciones propias del lenguaje que lo resuelvan
 *   automáticamente.
 */
"""

def ordenar_lista(lista, orden):
    largo = len(lista)
    if orden == "Asc":
        for i in range (0, largo):
            for j in range (0, largo):
                if lista[i] < lista[j]:
                    lista[i] , lista[j] = lista[j], lista[i]
        
    elif orden == "Desc":
        for i in range (0, largo):
            for j in range (0, largo):
                if lista[i] > lista[j]:
                    lista[i] , lista[j] = lista[j], lista[i]
    
    return lista


lista = [1, 5, 4, 10, 6]

orden = "Desc"
resultado = ordenar_lista(lista, orden)
print(resultado)