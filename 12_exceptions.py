### Exception Handling ###

numberOne = 1
numberTwo = 5
print(numberOne+ numberTwo)

numberTwo = "Hola"

# try - except

try:
    print(numberOne+ numberTwo)
    print("No se ha producido error")
except :
    print("Se ha producido un error")


# try - except - esle

numberTwo = 2

try:
    print(numberOne+ numberTwo)
    print("No se ha producido error")
except :
    print("Se ha producido un error")
else:
    # Se ejecuta si no se produce error
    print("La ejecución continua correctamente")

    
# try - except - else - finally: 

numberTwo = "Hola"

try:
    print(numberOne+ numberTwo)
    print("No se ha producido error")
except :
    print("Se ha producido un error")
else:
    print("La ejecución continua correctamente")
finally:
    # El finally se ejecuta siempre
    print("Se ejecuta al final, dando igual si hay error o no")


print("#########################################")
print()

# Captura de expciones por tipo

numberTwo = "Hola"

try:
    print(numberOne+ numberTwo)
    print("No se ha producido error")
except TypeError: # El TypeError solo captura los errores de este tipo, los de tipo ValueError los continuaria pasando y el codigo petaria.
    print("Se ha producido un error")
else:
    print("La ejecución continua correctamente")

# Captura de la información de la excepción

try:
    print(numberOne+ numberTwo)
    print("No se ha producido error")
except ValueError as error: 
    print("Se ha producido un error")
    print(error) 
except Exception as random_error: 
    print("Se ha producido un error random")
    print(random_error) 


