minutos: int
valor: float = 50


minutos = int(input("Digite a quantidade de minutos: "))

if minutos > 100:
    valor = (minutos - 100) * 2 + 50

print("Valor a pagar: {:.2f}".format(valor))