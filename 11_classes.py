### Classes ###

class MyPerson: # Por buenas practicas, se tendria que poner las primeras letras de las clases en mayusculas.
    pass # La función pass del sistema lo que hace es que no de error si no ponemos nada 
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname 

my_person = MyPerson("Alex", "Lopez")
print(my_person.name)

##########################################3

class MyPerson: 
   
    def __init__(self, name, surname):
        self.full_name = (f"{name} {surname}")

    def walk (self):
        print(f"{self.full_name} está caminando")

my_person = MyPerson("Alex", "Lopez")
print(my_person.full_name)
my_person.walk()  

##########################################3

class MyPerson: 
   
    def __init__(self, name, surname, alias = "Sin alias"):
        self.full_name = (f"{name} {surname} {alias}")

    def walk (self):
        print(f"{self.full_name} está caminando")

my_person = MyPerson("Alex", "Lopez")
print(my_person.full_name)
my_person.walk()  

my_other_person = MyPerson("Alex", "Perez", "alopez-180")
print(my_other_person.full_name)
my_other_person.walk()