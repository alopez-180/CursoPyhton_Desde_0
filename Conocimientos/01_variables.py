# Variables

########################################

my_str_var = "My string variable"
print(my_str_var)

my_int_var = 1
print(my_int_var)

my_bool_var = True
print(my_bool_var)

########################################

# Concat de cadenas
print(my_str_var, str(my_int_var),my_bool_var)
print("Este es el valor de:", my_bool_var)


print(type(my_int_var))
#######################################

#Conversión de int a str con la función "str"
int_to_string = str(my_int_var)
print(type(int_to_string))


#######################################

# Funciones del sistema
print(len(my_str_var)) #Cuenta los caracteres de una str

name = input("Dime tu nombre: ") #Introducimos a la variable, un str que nos proporciona el usuario por el terminal
print(name)


#######################################

# Variables en una sola línea
# ¡Cuidado con abusar de esta sintaxis! 

name, surname, alias, age = "Alex", "Lopez", "alopez-180", 20
print("Me llamo", name, surname, "y tengo", age, "años", "/", alias)


#######################################

# ¿Forzamos el tipo?
# En python no se puede forzar el tipo de una variable, pero se puede hacer que de una idea de lo que nosotros
# queremos que sea esa variable

address: str = "Mi dirección"
print(type(address)) 
address = 2
print(type(address))

