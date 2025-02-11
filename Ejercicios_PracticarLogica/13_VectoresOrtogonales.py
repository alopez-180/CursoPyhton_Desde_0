"""
/*
 * Crea un programa que determine si dos vectores son ortogonales.
 * - Los dos array deben tener la misma longitud.
 * - Cada vector se podría representar como un array. Ejemplo: [1, -2]
 */"""

# https://matematix.org/vectores-ortogonales/

# Supongamos que tenemos los vectores v = (1, 2) y w = (-2, 1). Para comprobar si son ortogonales, calculamos su producto
#  escalar:    v · w = (1)(-2) + (2)(1) = -2 + 2 = 0.


v = [1, 2]
w = [-2, 1]

lista = []
suma_vectores = 0

if (len(v) == len(w)):
    for i in range (len(v)):
        multiplicar = v[i] * w[i]
        lista.append(multiplicar)
    for i in range (len(lista)):
        suma_vectores += lista[i]
else:
    print("Error")


if suma_vectores == 0:
    print("Los vectores son ortogonales, ya que dan 0")
else:
    print(f"Los vectores no son ortogonales, dan {suma_vectores}")