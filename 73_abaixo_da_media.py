mediaVetor: float  = 0
somaVetor: float = 0
i: int
n: int
abaixoMedia: bool = False

n = int(input("Quantos numeros voce vai digitar?  "))

while n <= 0 or n > 10:
    n = int(input("Quantos numeros voce vai digitar?  "))

vetNumeros: float = [0 for x in range(n)]

for i in range(0, n):
    vetNumeros[i] = float(input("Digite um numero: ").replace(',', '.'))

for i in range(0, n):
    somaVetor = somaVetor + vetNumeros[i]

print()

mediaVetor = float(somaVetor / n)

print("MEDIA DO VETOR = {:.3f}".format(mediaVetor))

for i in range(0, n):
    if vetNumeros[i] < mediaVetor:
        abaixoMedia = True

if abaixoMedia == True:
    print("ELEMENTOS ABAIXO DA MEDIA: ")

for i in range(0, n):
    if vetNumeros[i] < mediaVetor:
        print(vetNumeros[i])