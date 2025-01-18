### Strings ###

my_string = "My String"
my_other_string = "Mi otro string"

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)
print(my_string , my_other_string)

my_new_line_string = "Este es un String\ncon salto de línea"
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulación"
print(my_tab_string)

my_scape_string = "\tEste es un String  \n escapado"
print(my_scape_string)

### Formateo ###

# Esta seria la forma correcta de formatear strings
name , surname , age = "Alex", "Lopez", 20
print("Mi nombre es {} {} y mi edad es {}" .format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" %(name , surname , age))


# Esta manera no seria una buena practica: 
print("Mi nombre es" + " " + name + " " + surname + " " + "y mi edad es" + " " + str(age)) 


# Inferencia de datos:
print(f"Mi nombre es {name} {surname} y mi edad es {age}")


# Desempaquetado de caracteres
lenguage = "Python"
a , b , c , d , e , f = lenguage
print(a)
print(e)

# División
lenguage_slice = lenguage[1:3] #Va del caracter 1 al 3, *Se cuenta desde el caracter 0* la y de python es el caracter 1
print(lenguage_slice)

lenguage_slice = lenguage[1:] #Va del caracter 1 al final
print(lenguage_slice)

lenguage_slice = lenguage[1] #Solo coje el caracter 1
print(lenguage_slice)

lenguage_slice = lenguage[-2] #Coje el segundo caracter empezando por el final
print(lenguage_slice)

lenguage_slice = lenguage[0:6:2] #Vamos del caracter 0 al 6, pero saltamos 1 y cojemos el siguiente (cada dos), es decir cojeremos el 0, el 2, y el 4
print(lenguage_slice)


# Reverse
reversed_language = lenguage[::-1]
print(reversed_language)

# Funciones del Sistema

print(lenguage.capitalize())
print(lenguage.upper())
print(lenguage.count("t"))
print(lenguage.isnumeric())
print("1".isnumeric())
print(lenguage.lower())
print(lenguage.upper().isupper())