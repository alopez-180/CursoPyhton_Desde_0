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

print("Alex" in my_other_dict) # Esta operación dara False, porque realmente "Alex" existe como valor y no como clave.

