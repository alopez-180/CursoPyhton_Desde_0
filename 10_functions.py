### Functions ###


def my_function ():
    print("Esto es una funcion")



my_function()

def sum_two_values (primer_numero, segundo_numero):
    print(primer_numero + segundo_numero)


sum_two_values(1,5)
sum_two_values(100,5)
sum_two_values("5","7")
sum_two_values(2,4.3)

def sum_two_values_with_return (primer_numero, segundo_numero):
    return (primer_numero + segundo_numero)

my_result = sum_two_values_with_return(10, 5)
print(my_result)


def print_name (name, surname):
    print(f"{name} {surname}")

print_name(surname="Lopez", name="Alex")

def print_name_with_default (name, surname, alias ="Sin alias"):
    print(f"{name},{surname},{alias}")

print_name_with_default(name="Alex", surname="Lopez")