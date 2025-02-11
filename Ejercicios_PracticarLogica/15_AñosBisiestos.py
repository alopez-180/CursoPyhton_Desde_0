"""
/*
 * Crea una función que imprima los 30 próximos años bisiestos
 * siguientes a uno dado.
 * - Utiliza el menor número de líneas para resolver el ejercicio.
 */
 """


def calcular_bisiestos (año):
    entre_quatro = año % 4
    entre_cien =  año % 100
    entra_quatrocientos = año % 400

    if ((entre_quatro == 0) and entre_cien != 0 or entra_quatrocientos == 0):
        print(f"El año {año} es bisiesto")
    else:
        print(f"El año {año} no bisiesto")


calcular_bisiestos(2345)