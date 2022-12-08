i: int = 0
n: int = 0
j: int = 0
posicao: int = 0
maiorNumero: float = 0

n = int(input("Quantos numeros voce vai digitar?  "))

while n <= 0 or n > 10:
    n = int(input("Quantos numeros voce vai digitar?  "))

vetNumero: float = [0 for x in range(n)]

for i in range(0, n):
    vetNumero[i] = float(input("Digite um numero: ").replace(',', '.'))

for i in range(0, n):
    for j in range(0, n):
        if vetNumero[i] >= vetNumero[j] and vetNumero[i] >= maiorNumero:
            maiorNumero = vetNumero[i]
            posicao = i

print("MAIOR VALOR = {}".format(maiorNumero))
print()
print("POSICAO DO MAIOR VALOR = {}".format(posicao))