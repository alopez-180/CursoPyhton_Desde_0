"""
/*
 * Dado un listado de números, encuentra el SEGUNDO más grande
 */
"""

def segundo (lista):

    # Borramos los duplicados
    for i in lista:
        if lista.count(i) > 1:
            lista.remove(i)

    # Ordenamos la lista
    for i in range(0, len(lista)):
        for j in range (0, len(lista)):
            if lista[i] < lista[j]:
                lista [i], lista[j] = lista[j], lista[i]
    
    # Con la lista ordenada, cojemos el segundo más alto
    segundo_valor = lista[-2]
    print(f" El segundo valor más grande es: {segundo_valor}")


lista = [100, 102, 102 , 2 , 5 , 102 , 3 , 3 , 6]

segundo(lista)