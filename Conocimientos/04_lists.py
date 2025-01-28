### Listas ###

my_list = list()
my_other_list = []

print(type(my_list))
print(type(my_other_list))

my_list = list("Hola") #Este formato de list lo que hace es cada caracter y ponerlo como elementos separados
print(my_list)

my_other_list = ["Hola" , "Adiós", 234, 23, 11] #Este formato, coje cada string o int que le ponemos como elemento de la lista
print(my_other_list) # Imprimimos todos los elementos de la lista
print(my_other_list[0]) # Imprimimos solo el elemeto 0 de la lista
print(my_other_list[-3]) # Imprimimos el valor tres empezando por el ultimo elemento de de la lista y contando desde 1, y no 0 como en el principio de la lista
print(my_other_list.count("Hola"))

my_personal_list = ["Alex", "Lopez", "20", "Spain"]
name , surname , age , location = my_personal_list 
# name , surname , age  = my_personal_list Este formato daria error, porque estamos intentando desempaquetar todos los paquetes en solo tres vairables, y la lista son 4
print(name)
print(location)
print(my_list + my_other_list) # Podemos juntar los elementos de una lista con otra

my_other_list.append("Elemento añadido") #Podemos añadir elementos con la función append.
print(my_other_list)

my_other_list.insert(1,"Azul") #Añadimos en la posición 1 un nuevo elemento y desplazamos el resto.
print(my_other_list) 

my_other_list[1] = "Rojo" #Le cambiamos el valor del elemento que esta en el indice 1 por el valor "Rojo"
print(my_other_list)

my_other_list.remove("Rojo") #Eliminamos un elemento de la lista concreto buscandolo por su valor y no por indice ( Y si hay más de uno, elimina el primero que encuentra).
print(my_other_list)

my_other_list.pop() #La función del pop elimina el ultimo elemento por defecto
print(my_other_list)

my_other_list.pop(1) #También le podemos especificar el elemento concreto que queremos borrar.
print(my_other_list)

del my_other_list[-1] #Con el del también podemos eliminar el elemento de la lista que nosotros especifiquemos.
print(my_other_list)

my_other_list.reverse() #Le damos la vuelta a los elementos de la lista.
print(my_other_list)

my_number_list = [18,4,6,2344,75,2,6,11] #Ordenamos la lista de menor a mayor.
my_number_list.sort()
print(my_number_list)

print(my_number_list[1:3]) #Buscamos los valores que hay entre la posición 1 y la tres

my_other_list.clear() #Limpiar una lista entera
print(my_other_list)

