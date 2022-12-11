m: int
i: int
n: int
j: int
somaLinhas: int = 0
temNegativo: bool = False

m = int(input("Qual a quantidade de linhas da matriz? "))
while m <= 0 or m > 10:
    m = int(input("Qual a quantidade de linhas da matriz? "))

n = int(input("Qual a quantidade de colunas da matriz? "))
while n <= 0 or n > 10:
    n = int(input("Qual a quantidade de colunas da matriz? "))

mat: int = [[0 for x in range(n)] for x in range(m)]

for i in range(0, m):
    print()
    for j in range(0, n):
        mat[i][j] = int(input("Elemento [{},{}]:".format(i,j)))

for i in range(0, m):
    print()
    for j in range(0, n):
        if mat[i][j] < 0:
            temNegativo = True

if temNegativo:
    print("VALORES NEGATIVOS: ")

for i in range(0, m):
    for j in range(0, n):
        if mat[i][j] < 0:
            print("{}".format(mat[i][j]))