m: int = 0
i: int = 0
n: int = 0
j: int = 0

m = int(input("Qual a quantidade de linhas da matriz? "))
while m <= 0 or m > 10:
    m = int(input("Qual a quantidade de linhas da matriz? "))

n = int(input("Qual a quantidade de colunas da matriz? "))
while n <= 0 or n > 10:
    n = int(input("Qual a quantidade de colunas da matriz? "))

matA: int = [[0 for x in range(n)] for x in range(m)]
matB: int = [[0 for x in range(n)] for x in range(m)]
matSoma: int = [[0 for x in range(n)] for x in range(m)]

print("Digite os valores da matriz A: ")

for i in range(0, m):
    for j in range(0, n):
        matA[i][j] = int(input("Elemento [{},{}]:".format(i,j)))

print("Digite os valores da matriz B: ")

for i in range(0, m):
    for j in range(0, n):
        matB[i][j] = int(input("Elemento [{},{}]:".format(i,j)))

for i in range(0, m):
    for j in range(0, n):
        matSoma[i][j] = matA[i][j] + matB[i][j]

print("MATRIZ SOMA: ")

for i in range(0, m):
    for j in range(0, n):
        print("{} ".format(matSoma[i][j]), end="")
    print()