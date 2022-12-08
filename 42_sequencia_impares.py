x: int
i: int

x = int(input("Digite o valor de X ou 0 para finalizar: "))

while (x != 0):
    for i in range(0, x):
        if i % 2 != 0:
            print(i)

    x = int(input("Digite o valor de X ou 0 para finalizar: "))