X: int
soma: int

X = int(input("Digite um numero inteiro: "))

while X != 0:
    if X % 2 != 0:
        X = X + 1

    soma = 5 * X + 20
    print("SOMA = {}".format(soma))
    X = int(input("Digite um numero inteiro: "))