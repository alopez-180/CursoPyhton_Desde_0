### Tuples ###


# Podemos definir las tuplas de las siguientes dos formas:
my_tuple = tuple()
my_other_tuple = ()


my_tuple = ("Hola", "Adios", 24, 45)
print(my_tuple)
print(my_tuple[3]) #Imprimimos el elemento de la posición tres

print(my_tuple.count("Hola")) #Nos cuenta cuatos elementos hay que coincidan con "Hola"
print(my_tuple.index(45)) #Nos dice en que indice se encuentra el elemento 45, si hubiese más de uno, solo nos diria indice del primer elemento


# my_tuple[1] = "Rojo"  Esta linea daría error, las tuplas no soportan cambios de elementos, son inmutables y constantes.


my_other_tuple = ("Alex", "Lopez", "20") 
my_sum_tuple = (my_tuple + my_other_tuple) #Aunque las tuplas sean inmutables, si que se pueden sumar con otras tuplas
print(my_sum_tuple)

print(my_sum_tuple[3:6])