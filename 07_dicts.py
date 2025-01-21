### Diccionarios ###

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = { # Con los diccionarios podemos almacenar datos de clave valor
    "Nombre":"Alex", 
    "Apellido":"Lopez", 
    "Edad":20, 
    "Lenguajes": {"Python","CSS","Java"},
    1:1.77}

print(my_other_dict)
print(len(my_other_dict)) #Nos da que la largada del diccionario són 5, porque solo cuenta las claves, y no el total de valores 

######################################

print(my_other_dict["Lenguajes"])
my_other_dict["Nombre"] = "Pedro"
print(my_other_dict)
my_other_dict["Calle"] = "Calle Alex"
print(my_other_dict)

del my_other_dict["Calle"] # Se pueden eliminar claves y automaticamente los elementos de dentro de la clave con "del"
print(my_other_dict)

######################################

print("Pedro" in my_other_dict) # Esta operación dara False, porque realmente "Pedro" existe como valor y no como clave.
print("Pedro" in my_other_dict["Nombre"]) # Esta operación dara True, porque dentro de la clavo Nombre, si que existe el elemento "Pedro"

print("#################")

print(my_other_dict.items()) # Nos ordena por lista la clave y el valors
print(my_other_dict.keys()) # Nos devuelve unicamente las claves que tenemos
print(my_other_dict.values()) # Nos devuelve los elementos que tenemos


my_other_dict = (dict.fromkeys(("Nombre", 1))) # El "fromkeys" lo que hace es crear claves con valores vacios 
print(my_other_dict)

my_other_dict = ["Nombre", 1, "Apellido"]
my_other_dict = (dict.fromkeys(my_other_dict))
print(my_other_dict)

my_other_dict["Nombre"] = "Alex" , "Pepe"
print(my_other_dict)

my_other_dict["Nombre"] = "Alex" , "Pepe"
print(my_other_dict)