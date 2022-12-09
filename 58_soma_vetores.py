i: int = 0
n: int = 0
j: int = 0

n = int(input("Quantos numeros voce vai digitar?  "))

while n <= 0 or n > 10:
    n = int(input("Quantos numeros voce vai digitar?  "))

vetNumeroA: int = [0 for x in range(n)]
vetNumeroB: int = [0 for x in range(n)]
vetNumeroC: int = [0 for x in range(n)]

print("Digite os valores do vetor A: ")
for i in range(0, n):
    vetNumeroA[i] = int(input())

print("Digite os valores do vetor B: ")
for i in range(0, n):
    vetNumeroB[i] = int(input())

for i in range(0, n):
    vetNumeroC[i] = vetNumeroA[i] + vetNumeroB[i]

print("VETOR RESULTANTE:")
for i in range(0, n):
    print(vetNumeroC[i])