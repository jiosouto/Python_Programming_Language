N: int
i: int
x: int

N = int(input("Quantos numeros voce vai digitar? "))

for i in range(0, N):
    x = int(input("Digite um numero: "))

    if x == 0:
        print("NULO")

    elif x % 2 == 0:
        if x < 0:
            print("PAR NEGATIVO")
        else:
            print("PAR POSITIVO")

    elif x < 0:
        print("IMPAR NEGATIVO")
    else:
        print("IMPAR POSITIVO")