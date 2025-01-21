

texto = input("Introduce un caracter para convertir en mayuscula: ")

array = []



for i in texto:
    if i == " ":
        print()
    else:
        i = ord(i)
        array.append(i)

print(array)

mayusculas = []

for i in (array):
    if (i > 96 and i < 123):
        i = i - 32
        i = chr(i)
        mayusculas.append(i)

print(mayusculas)