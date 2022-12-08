i: int = 0
n: int = 0
j: int = 0
somaDiagonalPrincipal: int = 0
controleSoma: int = 0;

n = int(input("Qual a quantidade de colunas da matriz? "))
while n <= 0 or n > 10:
    n = int(input("Qual a quantidade de colunas da matriz? "))

mat: int = [[0 for x in range(n)] for x in range(n)]

for i in range(0, n):
    for j in range(0, n):
        mat[i][j] = int(input("Elemento [{},{}]: ".format(i,j)))

for i in range(0, n):
    for j in range(i + 1, n):
        somaDiagonalPrincipal = somaDiagonalPrincipal + mat[i][j]

print("SOMA DOS ELEMENTOS ACIMA DA DIAGONAL PRINCIPAL = {}".format(somaDiagonalPrincipal))