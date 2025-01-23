### Conditionals ###

my_condition = True

if my_condition:
    print("Se ejecuta la condición del if")

###############

my_condition = 2 * 5
if my_condition == 11:
    print("Se ejecuta la segunda condición del if")

if my_condition == 10:
    print("Se ejecuta la tercera condición del if")

if my_condition > 10:
    print("Se ejecuta si my_condition es mayor que 10")
else:
    print("Es menor que 10")


my_condition = 20
if my_condition >= 10 and my_condition <= 20:
    print("El numero de my_condition es un numero entre 10 y 20")


my_condition = "Hola"
if my_condition: 
    print("Hola")


my_condition = ""
if not my_condition: # Esto especifica que la cadena de texto es vacia 
    print("Hola 2")