"""
/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
"""

# Aritmeticos

suma = 1 + 1
print(suma)
resta = 1 - 1
print(resta)
division = 5 / 3 # El resultado pude ser float, sin redondear
print(division)
division_entera = 5 // 3 # El resultado es entero, se redondea
print(division_entera)
multiplicacion = 3 * 5
print(multiplicacion)
modulo = 4 % 5
print(modulo)
exponente = 4**2
print(exponente)

# Comparadores

print(f"Igualdad 10 == 3 = {10 == 3}")
print(f"Igualdad 10 == 10 = {10 == 10}")
print(f"Desigualdas 10 != 3 = {10 != 3}")
print(f"Mayor que 10 > 3 = {10 > 3}")
print(f"Menor que 10 < 3 = {10 < 3}")
print(f"Mayor o igual que 10 >= 10 = {10 >= 10}")
print(f"Menor o igual que 10 <= 3 = {10 <= 3}")

# Logicos

print(f" AND: 10 + 3 == 13 and 5 - 1 == 4: {10 + 3 == 13 and 5 - 1 == 4}")
print(f" OR: 10 + 6 == 13 or 5 - 1 == 4: {10 + 6 == 13 or 5 - 1 == 4}")
print(f" NOT: not 10 + 3 == 13: {not 10 + 3 == 13 }")
print(f" NOT: not 10 + 3 == 16: {not 10 + 3 == 16 }")

# Operadores de asignación

my_number = 11 # asignación de un numero a una variable
my_number += 1 # suma y asignación
print(my_number)
my_number -= 1 # resta y asignación
print(my_number)
my_number *= 2 # multiplicación y asignación
print(my_number)
my_number /= 2 # división y asignación
print(my_number)
my_number **= 2 # Exponente y asignación
print(my_number)
my_number //= 2 # división entera y asignación
print(my_number)
my_number %= 2 # modulo y asignación
print(my_number)

# Operadores de identidad

my_new_number = 1.0 # La identidad lo que intenta comparar es el valor en memoria
print(f"my_number is my_new_nuber es {my_number is my_new_number}")
my_new_number = my_number
print(f"my_number is my_new_nuber es {my_number is my_new_number}")
my_new_number = 1.0
print(f"my_number is not my_new_nuber es {my_number is not my_new_number}")

# Operadores de pertenencia

print(f" La letra u esta en la palabra Moure? {'u' in 'moure'}") # Hay que ponerlo entre comillas simples, 'u' y 'moure' si no da error.
print(f" La letra u esta en la palabra Moure? {'b' not in 'moure'}") 
print(f" La letra u esta en la palabra Moure? {'b' not in 'bajada'}") # Da false porque si que hay una b en la palabra "Bajada"

# Opedadores de bit

a = 10  #1010
b = 3   #0011
print(F" AND: 10 & 3 = {10 & 3}") #La funcion and va a ir comparando bit a bit, i si los dos bits son 1 el bit resultante es uno
# si no de lo contrario sera 0

#1010 -- 0011, de derecha a izquierda, 1 y 0 = 0, 1 y 1 = 1, 0 y 0 = 0, y 0 y 1 = 0. El resultado es 0010, y esto si lo convertimos de binario es 2

print(F" OR: 10 | 3 = {10 | 3}") # El or compara bit a bit, y si almenos alguno de los dos bits es 1, el resultado es 1

#1010 -- 0011, de derecha a izquierda, 1 y 0 = 1, 1 y 1 = 1, 0 y 0 = 0, y 0 y 1 = 1. El resultado es 1011, y esto si lo convertimos de binario es 11

print(F" XOR: 10 ^ 3 = {10 ^ 3}") # El xor compara bit a bit, y si los dos bits son diferentes, el resultado es 1

#1010 -- 0011, de derecha a izquierda, 1 y 0 = 1, 1 y 1 = 0, 0 y 0 = 0, y 0 y 1 = 1. El resultado es 1001, y esto si lo convertimos de binario es 9

print(F" NOT: ~10 = {~10}") #Aqui lo que se hace es invertir la representación bit a bit, sobre el numero 10
#1010 --> 0101, despues le sumamos 1 que da 01011, y esto nos da el numero 11

print(f"Desplazamiento a la derecha: 10 >> 2 = {10 >> 2}") # La representación de 10 en bits es 1010, si pasamos todos los bits
# a la derecha contando dos, como hemos puesto, pasaria a ser 0010, esto da 2. AL DESPLAZAR LOS BITS A LA DERECHA, SE PIERDEN POR ESO ES 0010 Y NO 001010

print(f"Desplazamiento a la izquieda: 10 << 2 = {10 << 2}") # La representación de 10 en bits es 1010, si pasamos todos los bits
# a la derecha contando dos, como hemos puesto, pasaria a ser 101000, esto da 40. 


"""
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
"""

# Condicionales

my_string = "MoureDev"

if my_string == "Alex":
    print("My_string tiene el valor Alex")

elif (my_string == "MoureDev"):
    print("My_string tiene el valor de MoureDev ")

else:
    print("My_string tiene un valor diferente que no es ni Alex ni MoureDev")

# Iterativas

for i in range (11):
    print(i, end=" ")
print()

i = 0
while i <= 10:
    print(i, end=" ")
    i +=1
print()

# Manejo de excepciones

try:
    print(10 / 0)
except:
    print("Se ha producido un error")
finally:
    print("Ha finalizado el manejo de excepciones")


"""
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */
"""

for i in range (10,56):
    if (i % 2 == 0 and i != 16 and i % 3 != 0):
        print(i)
