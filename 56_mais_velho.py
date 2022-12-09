i: int = 0
n: int = 0
j: int = 0
posicaoMaisVelho: int = 0

n = int(input("Quantas pessoas voce vai digitar? "))

while n <= 0 or n > 10:
    n = int(input("Quantas pessoas voce vai digitar? "))

vetIdade: int = [0 for x in range(n)]
vetNome: str = [0 for x in range(n)]

for i in range(0, n):
    print("Dados da {} a pessoa: ".format(i + 1))
    vetNome[i] = input("Nome: ")

    vetIdade[i] = int(input("Idade: "))
    print()

for i in range(0, n):
    for j in range(0, n):
        if vetIdade[i] >= vetIdade[j] and vetIdade[i] >= vetIdade[posicaoMaisVelho]:
            posicaoMaisVelho = i

print("PESSOA MAIS VELHA: {}".format(vetNome[posicaoMaisVelho]))