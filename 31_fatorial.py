N: int
i: int
fat: int

N = int(input("Digite o valor de N: "))

if N <= 15:
    fat = 1

    for i in range(1, N + 1):
        fat = fat * i

    print("FATORIAL = {}".format(fat))

else:
    print("Valor precisa ser menor ou igual a 15")