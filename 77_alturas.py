i: int = 0
n: int = 0
somaMaiorIdade: int = 0
somaAltura: float = 0
mediaAltura: float = 0
porcentagemMenorIdade: float = 0;

n = int(input("Quantos numeros voce vai digitar?  "))

while n <= 0 or n > 10:
    n = int(input("Quantos numeros voce vai digitar?  "))

vetAltura: float = [0 for x in range(n)]
vetIdade: int = [0 for x in range(n)]
vetNome: str = [0 for x in range(n)]

for i in range(0, n):
    print("Dados da {} a pessoa: ".format(i + 1))
    vetNome[i] = input("Nome: ")
    vetIdade[i] = int(input("Idade: "))
    vetAltura[i] = float(input("Altura: ").replace(',', '.'))
    print(" ")

for i in range(0, n):
    somaAltura = somaAltura + vetAltura[i]

mediaAltura = float(somaAltura / n)

print("Altura média: {:.2f}".format(mediaAltura))

for i in range(0, n):
    if vetIdade[i] < 16:
        somaMaiorIdade = somaMaiorIdade + 1

porcentagemMenorIdade = float((somaMaiorIdade * 100) / n);

print("Pessoas com menos de 16 anos: {:.1f}%".format(porcentagemMenorIdade))

for i in range(0, n):
    if vetIdade[i] < 16:
        print("{}".format(vetNome[i]))