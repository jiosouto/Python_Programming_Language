somaVetor: int = 0
i: int = 0
n: int = 0
contPar: int = 0
mediaPares: float = 0
temPar: bool = False

n = int(input("Quantos numeros voce vai digitar?  "))

while n <= 0 or n > 10:
    n = int(input("Quantos numeros voce vai digitar?  "))

vetNumeros: int = [0 for x in range(n)]

for i in range(0, n):
    vetNumeros[i] = float(input("Digite um numero: ").replace(',', '.'))

for i in range(0, n):
    if vetNumeros[i] % 2 == 0:
        somaVetor = somaVetor + vetNumeros[i]
        temPar = True
        contPar = contPar + 1

if not temPar:
    print("NENHUM NUMERO PAR")

else:
    mediaPares = float(somaVetor / contPar)
    print("MEDIA DOS PARES = {:.1f}".format(mediaPares))