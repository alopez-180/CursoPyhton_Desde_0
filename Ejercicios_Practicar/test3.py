
## Cuadrado ##

tamaño = 5

for i in range (tamaño):
    for j in range (tamaño):
        if ((i == tamaño-1) or i == 0 or j == 0 or (j == tamaño-1)):
            print("*",end=" ")
        else:
            (print(" ", end=" "))
    print(" ")

print("###############")

## Triangulo ##

tamaño = 5

for i in range (tamaño):
    for j in range (tamaño-i-1):
        print(" ",end=" ")
    for k in range (2*i+1):
        print("*", end=" ")
    print(" ")

    
print("###############")

## Rombo ## 

for i in range (tamaño):
    for j in range (tamaño-i-1):
        print(" ",end=" ")
    for k in range (2*i+1):
        print("*", end=" ")
    print()
for i in range (tamaño):
    for j in range (tamaño-i-1):
        print(" ", end=" ")
    for k in range (2 * i + 1):
        print("*", end=" ")
    print()
           