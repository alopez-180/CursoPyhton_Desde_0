"""
/*
 * ¿Conoces el calendario de aDEViento de la comunidad (https://adviento.dev)?
 * 24 días, 24 regalos sorpresa relacionados con desarrollo de software.
 * Desde el 1 al 24 de diciembre.
 *
 * Crea un programa que simule el mecanismo de participación:
 * - Mediante la terminal, el programa te preguntará si quieres añadir y borrar
 *   participantes, mostrarlos, lanzar el sorteo o salir.
 * - Si seleccionas añadir un participante, podrás escribir su nombre y pulsar enter.
 * - Si seleccionas añadir un participante, y este ya existe, avisarás de ello.
 *   (Y no lo duplicarás)
 * - Si seleccionas mostrar los participantes, se listarán todos.
 * - Si seleccionas eliminar un participante, podrás escribir su nombre y pulsar enter.
 *   (Avisando de si lo has eliminado o el nombre no existe)
 * - Si seleccionas realizar el sorteo, elegirás una persona al azar
 *   y se eliminará del listado.
 * - Si seleccionas salir, el programa finalizará.
 */
"""

import random
import time
import os

continua = True
participantes = []

while continua:
    print("*************************")

    print("1- Añadir participante")
    print("2- Mostrar participantes")
    print("3- Eliminar participante")
    print("4- Realizar el sorteo")
    print("5- Salir")

    print("*************************")
    
    opcion = int(input("Selecciona una opción: "))

    os.system('cls')

    if (opcion == 1):
        participante = str(input("Nombre del participante que deseas añadir: "))
        if (participantes.count(participante) >= 1):
            print("Ya hay un participante registrado con ese nombre")
        else:
            participantes.append(participante)
        
        time.sleep(2)
    
    elif (opcion == 2):
        print("Participantes: ")
        count = 1
        for i in participantes:
            print(f" {count}- {i}")
            count +=1

        time.sleep(2)
            
    elif (opcion == 3):
        usuario_eliminar = str(input("Que participante deseas eliminar? "))
        if (participantes.count(usuario_eliminar) != 1):
            print("No existe un participante con ese nombre")
        else:
            index = participantes.index(usuario_eliminar)
            participantes.pop(index)
            print(f"Usuario {usuario_eliminar} eliminado correctamente")

        time.sleep(2)
   
    elif (opcion == 4):
        num_participantes = len(participantes)
        num_ganador = random.randint(1, num_participantes)
        print(num_ganador)
        ganador = participantes[num_ganador]
        print(f"El ganador del sorteo es: {ganador}")
        participantes = []

        time.sleep(2)
   
    elif (opcion == 5):
        continua = False
        print("Saliendo")
   
    else: 
        print("Error")
