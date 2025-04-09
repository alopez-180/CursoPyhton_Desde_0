"""
/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet)
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */
"""

dict_leen = {"A":"4", "B":"I3" , "C":"[" , "D":")", "E":"3" , "F":"|=" , "G":"&" ,
            "H":"#" , "I":"1" , "J":",_|" , "K":">|" , "L":"1" , "M":"/\/\\" , "N":"^/" ,
            "O":"0" , "P":"|^*", "Q":"(_,)" , "R":"I2" , "S":"5" , "T":"7" , "U":"(_)" , 
            "V":"\/" , "W":"\/\/" , "X":"><" , "Y":"j" , "Z":"2" , "1":"L" , "2":"R" , 
            "3":"E" , "4":"A" , "5":"S" , "6":"b" , "7":"T" , "8":"B" , "9":"g" , "0":"o"}


str1 = str(input(f"Introduce una cadena de texto: "))
str1 = str1.upper()
cadena = ""

for i in str1:
    a = (i in dict_leen)

    if (a == False):
       cadena = cadena + i
    else:
        i = dict_leen[i]
        cadena = cadena + i 

print(cadena)


