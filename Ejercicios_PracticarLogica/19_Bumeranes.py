"""
/*
 * Crea una función que retorne el número total de bumeranes de
 * un array de números enteros e imprima cada uno de ellos.
 * - Un bumerán (búmeran, boomerang) es una secuencia formada por 3 números
 *   seguidos, en el que el primero y el último son iguales, y el segundo
 *   es diferente. Por ejemplo [2, 1, 2].
 * - En el array [2, 1, 2, 3, 3, 4, 2, 4] hay 2 bumeranes ([2, 1, 2]
 *   y [4, 2, 4]).
 */
"""

def bumeranes (lista):
    bumeranes = []
    for i in range (len(lista)):
        if i < (len(lista)-2):
            if(lista[i] == lista[i+2] and lista[i] != lista[i-1]): 
                 for j in range (3):
                    bumeranes.append(lista[i])
                    i += 1              
            
    total_bumeranes = len(bumeranes) // 3
    count = 0
    print(f"Hay un total de {total_bumeranes} bumeranes:")
    print ("[", end=" ")
    for i in (bumeranes):
        if (1 % 3 != 0): 
            print(f"{i}", end=" ")
            count += 1
        else:
            print(f"{i}", end=" ")
            count += 1
        if (count % 3 == 0):
                print ("]")
                if count != len(bumeranes):
                    print ("[", end=" ")
                

lista = [2, 1, 2, 3, 3, 4, 2, 4, 5, 6, 5]
bumeranes(lista)