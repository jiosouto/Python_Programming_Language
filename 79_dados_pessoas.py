i: int = 0
n: int = 0
j: int = 0
totalHomens: int = 0
totalMulher: int = 0
menorAltura: float = 0
maiorAltura: float = 0
somaAlturaMulheres: float = 0
mediaAlturaMulheres: float = 0
temMulher: bool = False

n = int(input("Quantas pessoas voce vai digitar? "))

while n <= 0 or n > 10:
    n = int(input("Quantas pessoas voce vai digitar? "))

vetAltura: float = [0 for x in range(n)]
vetGenero: str = [0 for x in range(n)]

for i in range(0, n):
    vetAltura[i] = float(input("Altura da {}a pessoa: ".format(i + 1)).replace(',', '.'))
    vetGenero[i] = input("Genero da {}a pessoa: ".format(i + 1))

    while vetGenero[i] != 'F' and vetGenero[i] != 'f' and vetGenero[i] != 'm' and vetGenero[i] != 'M':
        vetGenero[i] = input("Genero da {}a pessoa: ".format(i + 1))
    print()

menorAltura = vetAltura[0]
menorAltura = vetAltura[0]
for i in range(0, n):
    for j in range(0, n):
        if vetAltura[i] <= vetAltura[j] and vetAltura[i] <= menorAltura:
            menorAltura = vetAltura[i]

for i in range(0, n):
    for j in range(0, n):
        if vetAltura[i] >= vetAltura[j] and vetAltura[i] >= maiorAltura:
            maiorAltura = vetAltura[i]

for i in range(0, n):
    if vetGenero[i] == 'F' or vetGenero[i] == 'f':
        somaAlturaMulheres = somaAlturaMulheres + vetAltura[i]
        temMulher = True
        totalMulher = totalMulher + 1
    elif vetGenero[i] == 'M' or vetGenero[i] == 'm':
        totalHomens = totalHomens + 1

print("Menor altura = {:.2f}".format(menorAltura))
print("Maior altura = {:.2f}".format(maiorAltura))

if temMulher == True:
    mediaAlturaMulheres = float(somaAlturaMulheres / totalMulher)
    print("Media das alturas das mulheres = {:.2f}".format(mediaAlturaMulheres))
else:
    print("Não foi possivel calcular media, mão há mulheres informadas")

print("Numero de homens = {}".format(totalHomens))