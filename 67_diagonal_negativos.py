i: int
n: int = 0
j: int
somaNegativos: int = 0

n = int(input("Qual a ordem da matriz? "))

while n <= 0 or n > 10:
    n = int(input("Qual a ordem da matriz? "))

mat: int = [[0 for x in range(n)] for x in range(n)]

for i in range(0, n):
    for j in range(0, n):
        mat[i][j] = int(input("Elemento [{},{}]: ".format(i,j)))

print("DIAGONAL PRINCIPAL:")
for i in range(0, n):
    print("{} ".format(mat[i][i]), end="")

print()

for i in range(0, n):
    for j in range(0, n):
        if mat[i][j] < 0:
            somaNegativos = somaNegativos + 1

print("QUANTIDADE DE NEGATIVOS = {}".format(somaNegativos))