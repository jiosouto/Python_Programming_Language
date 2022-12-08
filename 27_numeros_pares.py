i: int = 0
n: int = 0
somaPares: int = 0

n = int(input("Quantos numeros voce vai digitar?  "))

while n <= 0 or n > 10:
    n = int(input("Quantos numeros voce vai digitar?  "))

vetNumero: int = [0 for x in range(n)]

for i in range(0, n):
    vetNumero[i] = int(input("Digite um numero: "))

print()

print("NUMEROS PARES:")

for i in range(0, n):
    if vetNumero[i] % 2 == 0:
        print("{} ".format(vetNumero[i]), end="")
        somaPares = somaPares + 1

print()
print("QUANTIDADE DE PARES = {}".format(somaPares))