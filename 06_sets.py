### Sets ###

my_set = set()
my_other_set = {} # Esto inicialmente es un diccionario
print(type(my_other_set))

my_other_set = {"Alex", "Lopez", 35} # Esto es un set
print(type(my_other_set))



my_other_set.add("alopez-180") 
print(my_other_set) # Un set no es ordenado, nos añadira este valor donde quiera
my_other_set.add("alopez-180") # No se pueden añadir elementos repetidos, por mucho que le pongamos, solo pondra uno
print(my_other_set)

# print(my_other_set[3]) No se pueden acceder a los elementos por indice, ya que es un poco aleatorio

print("Alex" in my_other_set)
print("Moure" in my_other_set)

my_other_set.update("Alex") # Separa los caracteres del str que nosostros le especificamos
print(len(my_other_set))

my_other_set.remove("Alex") # Se pueden eliminar elementos
print(my_other_set)

my_other_set.clear() # Tambien se puede limpiar 
print(len(my_other_set))


my_set = {1,2,3,"Python"}
my_other_set = {"Alex", "Lopez", 35}

# print(my_set + my_other_set) # TypeError: unsupported operand type(s) for +: 'set' and 'set'

my_new_set = (my_set.union(my_other_set)) # Para unir sets, se tendria que hacer de esta manera. Y teniendo en cuenta que no se duplican.
print(my_new_set)

print(my_new_set.difference(my_set))


