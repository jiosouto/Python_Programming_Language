i: int
maior: int = 0
n: int
j: int

n = int(input("Qual a quantidade de colunas da matriz? "))
while n <= 0 or n > 10:
    n = int(input("Qual a quantidade de colunas da matriz? "))

mat: int = [[0 for x in range(n)] for x in range(n)]
maiorDaLinha: int = [[0 for x in range(n)] for x in range(n)]

for i in range(0, n):
    for j in range(0, n):
        mat[i][j] = int(input(f"Elemento [{i},{j}]: "))

for i in range(0, n):
    maior = mat[i][0]
    for j in range(0, n):
        if maior < mat[i][j]:
            maior = mat[i][j]

    maiorDaLinha[i] = maior

print()

print("MAIOR ELEMENTO DE CADA LINHA:")

for i in range(0, n):
    print("{}".format(maiorDaLinha[i]))