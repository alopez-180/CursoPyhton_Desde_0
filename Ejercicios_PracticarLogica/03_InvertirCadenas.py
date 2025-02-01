"""
/*
 * Crea un programa que invierta el orden de una cadena de texto
 * sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
 */
 """

cadena = "Hola mundo"
cadena_to_array = []
cadena_inversa = []

for i in cadena:
    cadena_to_array.append(i)

for i in range (len(cadena_to_array)):
    cadena_inversa.append(cadena_to_array[-1])
    cadena_to_array.pop(-1)

cadena_inversa = ''.join(cadena_inversa)
print(cadena_inversa)

#####################################################

cadena = "Hola mundo"

for i in cadena[::-1]:
    print(f"{i}", end="")

"""
secuencia[inicio:fin:paso]
inicio: Índice desde donde empezar (si se omite, empieza desde el inicio).
fin: Índice donde termina (si se omite, llega hasta el final).
paso: Indica el salto entre elementos (si es negativo, recorre en reversa).
"""