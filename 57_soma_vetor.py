soma: float = 0
media: float
i: int
n: int

n = int(input("Quantos numeros voce vai digitar?  "))

while n < 0 and n > 10:
    n = int(input("Quantos numeros voce vai digitar?  "))

vet: float = [0 for x in range(n + 1)]

for i in range(0, n):
    vet[i] = float(input("Digite um numero para somar: ").replace(',', '.'))

print("VALORES = ", end="")
for i in range(0, n):
    print("{:.1f} ".format(vet[i]), end="")

for i in range(0, n):
    soma = soma + vet[i]

media = float(soma / n)

print()
print("SOMA = {:.2f}".format(soma))
print("Media = {:.2f}".format(media))