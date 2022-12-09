n: int
i: int
temNegativo: bool = False

n = int(input("Quantos numeros voce vai digitar? "))

while n < 0 and n > 10:
    n = int(input("Quantos numeros voce vai digitar? "))

vet: int = [0 for x in range(n + 1)]


for i in range(1, n + 1):
    vet[i] = int(input("Digite um numero: "))

for i in range(1, n + 1):
    if vet[i] < 0:
        temNegativo = True

if temNegativo:
    print("Numeros negativos: ")
else:
    print("Não digitou numeros negativos: ")

for i in range(1, n + 1):
    if vet[i] < 0:
        print(vet[i])