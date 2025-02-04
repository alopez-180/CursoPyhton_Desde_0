"""
/*
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
 */
"""

## Triangulo:  Área = (base x altura) / 2
## Cuadrado:   Área = lado x lado
## Rectángulo: Área = base x altura

def calcular_area():
    tipo = str(input("Especifica el tipo de poligono que deseas calcular el area (Cuadrado, Triángulo y Rectángulo): "))
    tipo = tipo.lower()
    continua = True
    while continua:

        if (tipo == "triangulo" or tipo == "triángulo"):
            base = float(input("Introduce la base del triángulo: "))
            altura = float(input("Introduce la base del triángulo: "))
            area = ((base * altura) / 2)
            continua = False
            return area, tipo

        elif (tipo == "cuadrado"):
            lado = float(input("Introduce el lado del cuadrado: "))
            area = (lado * 4)
            continua = False
            return area, tipo
        
        elif (tipo == "rectángulo" or tipo == "rectangulo"):
            base = float(input("Introduce la base del rectangulo: "))
            altura = float(input("Introduce la altura del rectangulo: "))
            area = (base * altura)
            continua = False
            return area, tipo

        else:
            print("** ERROR **")
            tipo = str(input("Introduce un tipo de poligono admitido (Cuadrado, Triángulo y Rectángulo): "))

resultado = calcular_area()

print(f"El area de tu {resultado[1]} es: {resultado[0]} cm2")