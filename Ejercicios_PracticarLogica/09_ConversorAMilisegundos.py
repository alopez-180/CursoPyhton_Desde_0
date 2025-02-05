"""
/*
 * Crea una función que reciba días, horas, minutos y segundos (como enteros)
 * y retorne su resultado en milisegundos.
 */
"""

def conversor_milisegundos(tipo, tiempo):
    
    if (tipo == "dia" or tipo == "dias"):
        tiempo = tiempo * 24 # Pasamos de dias a horas
        milisegundos = tiempo * 3600000

    elif (tipo == "hora" or tipo == "horas"):
        milisegundos = tiempo * 3600000

    elif (tipo == "minuto" or tipo == "minutos"):
        tiempo = tiempo / 60
        milisegundos = tiempo * 3600000
    
    elif (tipo == "segundo" or tipo == "segundos"):
        tiempo = tiempo / 60 # Pasamos a minutos
        tiempo = tiempo / 60 # Pasamos a horas
        milisegundos = tiempo * 3600000
    else:
        print("Error")

    return milisegundos

tipo = str(input("Introduce si quieres convertir días, horas, minutos y segundos: "))
tiempo = int(input(f"Especifica el numero de {tipo}: "))

resultado = conversor_milisegundos(tipo, tiempo)
print(f"El resultado es: {resultado} ms")