x: int = 0
n: int = 0
dentro: int = 0
fora: int = 0
i: int = 0

while x == 0:
    n = int(input("Quantos numeros voce vai digitar? "))

    for i in range(0, n):
        x = int(input("Digite um numero: "))

        if x >= 10 and x <= 20:
            dentro = dentro + 1

        else:
            fora = fora + 1;

    print("{} DENTRO".format(dentro))
    print("{} FORA".format(fora))