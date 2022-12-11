N: int = 0
i: int
qte: int = 0
totalCobaias: int = 0
totalSapos: int = 0
totalCoelhos: int = 0
totalRatos: int = 0
tipoCobaiaCorreto: int = 0

pratos: float = 0
psapos: float = 0
pcoelhos: float = 0
tipoCobaia: str

N = int(input("Quantos casos de teste serao digitados? "))

while N <= 0:
    N = int(input("Digite um numero inteiro? "))

for i in range(1, N + 1):
    qte = int(input("Quantidade de cobaias: "))

    while qte <= 0:
        qte = int(input("Quantidade de cobaias: "))

    print("Digite o tipo de cobaia correto:")
    print("R para rato")
    print("S para sapo")
    print("C para coelho")
    tipoCobaia = input("Tipo de cobaia: ")

    if tipoCobaia == 's' or tipoCobaia == 'S':
        tipoCobaiaCorreto = 1

    elif tipoCobaia == 'c' or tipoCobaia == 'C':
        tipoCobaiaCorreto = 1

    elif tipoCobaia == 'r' or tipoCobaia == 'R':
        tipoCobaiaCorreto = 1

    else:
        tipoCobaiaCorreto = 0

    while tipoCobaiaCorreto == 0:
        print("Digite o tipo de cobaia correto:")
        print("R para rato")
        print("S para sapo")
        print("C para coelho")
        tipoCobaia = input("Tipo de cobaia: ")

        if tipoCobaia == 's' or tipoCobaia == 'S':
            tipoCobaiaCorreto = 1

        elif tipoCobaia == 'c' or tipoCobaia == 'C':
            tipoCobaiaCorreto = 1

        elif tipoCobaia == 'r' or tipoCobaia == 'R':
            tipoCobaiaCorreto = 1

        else:
            tipoCobaiaCorreto = 0

    if tipoCobaia == 's' or tipoCobaia == 'S':
        totalSapos = totalSapos + qte

    elif tipoCobaia == 'c' or tipoCobaia == 'C':
        totalCoelhos = totalCoelhos + qte

    elif tipoCobaia == 'r' or tipoCobaia == 'R':
        totalRatos = totalRatos + qte

totalCobaias = totalRatos + totalSapos + totalCoelhos

pcoelhos = float(totalCoelhos / totalCobaias * 100.0)
pratos = float(totalRatos / totalCobaias * 100.0)
psapos = float(totalSapos / totalCobaias * 100.0)

print("RELATORIO FINAL:")
print("Total: {} cobaias".format(totalCobaias))
print("Total de coelhos: {}".format(totalCoelhos))
print("Total de ratos: {}".format(totalRatos))
print("Total de sapos: {}".format(totalSapos))
print("Percentual de coelhos: {:.2f}".format(pcoelhos))
print("Percentual de ratos: {:.2f}".format(pratos))
print("Percentual de sapos: {:.2f}".format(psapos))