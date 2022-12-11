import math

i: int = 0
n: int = 0
j: int = 0
linhaEscolhida: int = 0
colunaEscolhida: int = 0
somaPositivos: float = 0

n = int(input("Qual a quantidade de colunas da matriz? "))
while n <= 0 or n > 10:
    n = int(input("Qual a quantidade de colunas da matriz? "))

mat: float = [[0 for x in range(n)] for x in range(n)]

for i in range(0, n):
    for j in range(0, n):
        mat[i][j] = float(input("Elemento [{},{}]: ".format(i,j)).replace(',', '.'))

print()

for i in range(0, n):
    for j in range(0, n):
        if mat[i][j] >= 0:
            somaPositivos = somaPositivos + mat[i][j]

print("SOMA DOS POSITIVOS: {:.1f}".format(somaPositivos))
print()

linhaEscolhida = int(input("Escolha uma linha: "))

print("LINHA ESCOLHIDA: ", end="")

for i in range(0, n):
    print("{:.1f} ".format(mat[linhaEscolhida][i]), end="")
print()
print()

colunaEscolhida = int(input("Escolha uma coluna: "))

print("COLUNA ESCOLHIDA: ", end="")

for i in range(0, n):
    print("{:.1f} ".format(mat[i][colunaEscolhida]), end="")

print()
print()
print()

print("DIAGONAL PRINCIPAL: ", end="")
for i in range(0, n):
    print("{:.1f} ".format(mat[i][i]), end="")

for i in range(0, n):
    for j in range(0, n):
        if mat[i][j] < 0:
            mat[i][j] = math.pow(mat[i][j], 2)
print()
print()
print("MATRIZ ALTERADA: ")

for i in range(0, n):
    for j in range(0, n):
        print("{:.1f} ".format(mat[i][j]), end="")
    print()