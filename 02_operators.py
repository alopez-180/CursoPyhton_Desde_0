### Operadores Aritmeticos ###

print( 3 + 4 ) # Suma
print( 3 - 4 ) # Resta
print( 3 * 4 ) # Multiplicación
print( 3 / 4 ) # División

###########################

print( 10 / 2)
print( 10 % 2)  # El modulo, es el resto que queda en una división

print( 10 / 3)
print( 10 % 3)

###########################

print( 10 // 3 ) # El // es una floor división, es decir aproximar el valor float a uno int

###########################

print( 2 ** 3) # Calcular el exponente, en este caso dos elevado a tres

###########################

print("Hola" + "Python")
print("Hola " * 5)
print("Hola " * (2**3))

my_float = (2.5 * 2) # Aunque dos coma cinco multiplicado por dos de cinco, el valor es 5.0, por lo que es un float.
my_int = int(my_float)
print("Hola " * my_int)


###########################

### Operadores Comparativos ###

print( 3 > 4)
print( 3 < 4)
print( 4 >= 4)
print( 10 <= 4)
print( 3 == 4)
print( 3 != 4)

print("#############")

# Por defecto con str, hace una comparación alfabetica por ASCII
print( "Hola" > "Python")
print( "Hola" < "Python")
print( "Hola" >= "Python")
print( "Hola" <= "Python")
print( "Hola" == "Python")
print( "Hola" != "Python")

print( "aaaa" >= "abaa") # Compara una ordenación alfabética
print(len("aaaa") >= len("aaaa")) # Cuenta caracteres
print( "Aaaa" >= "aaaa") # Las mayusculas y minusculas también son diferentes. 


###########################

### Operadores Lógicos ###

print(3 > 4 and "Hola" > "Python")
print(3 > 4 or "Hola" > "Python")
# print(3 > 4 not "Hola" > "Python")