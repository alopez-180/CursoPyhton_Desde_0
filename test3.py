

tamaño = 4


for i in range(tamaño):
    for j in range(tamaño):
        if i == 0 or i == tamaño - 1 or j == 0 or j == tamaño - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print("###################################")

for i in range(tamaño):
    for j in range(tamaño):
        if  j == 0 or j == tamaño - 1 or i == (tamaño // 2):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


print("###################################")

for i in range (tamaño):
    for j in range(tamaño-i-1):
        print(" ",end=" ")
    for k in range (2*i+1):
        print("*", end=" ")
    print()