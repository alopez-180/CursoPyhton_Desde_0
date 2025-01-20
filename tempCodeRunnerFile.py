for i in range(tamaño):
    for j in range(tamaño):
        if  j == 0 or j == tamaño - 1 or i == (tamaño // 2):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
