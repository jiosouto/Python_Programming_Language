i: int = 0
n: int = 0
somaAprovados: int = 0
temAprovado: bool = False

n = int(input("Quantas pessoas voce vai digitar? "))

while n <= 0 or n > 10:
    n = int(input("Quantas pessoas voce vai digitar? "))

mediasNotas: float = [0 for x in range(n)]
vetNota1: float = [0 for x in range(n)]
vetNota2: float = [0 for x in range(n)]
aprovados: str = [0 for x in range(n)]
vetNome: str = [0 for x in range(n)]

for i in range(0, n):
    print("Digite nome, primeira e segunda nota do {} o aluno: ".format(i + 1))
    vetNome[i] = input()
    vetNota1[i] = float(input().replace(',', '.'))
    vetNota2[i] = float(input().replace(',', '.'))

for i in range(0, n):
    mediasNotas[i] = float((vetNota1[i] + vetNota2[i]) / 2)

for i in range(0, n):
    if mediasNotas[i] >= 6:
        temAprovado = True
        aprovados[i] = vetNome[i]

print()
if temAprovado:
    print("Alunos aprovados: ")

for i in range(0, n):
    if mediasNotas[i] >= 6:
        print(aprovados[i])