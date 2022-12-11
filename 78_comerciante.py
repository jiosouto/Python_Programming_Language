i: int = 0
n: int = 0
j: int = 0
lucroMenor10: int = 0
lucroEntre10e20: int = 0
lucroAcima20: int = 0
valorTotalCompra: float = 0
valorTotalVenda: float = 0
valorTotalLucro: float = 0

n = int(input("Quantas pessoas voce vai digitar? "))

while n <= 0 or n > 10:
    n = int(input("Quantas pessoas voce vai digitar? "))

vetPrecoCompra: float = [0 for x in range(n)]
vetPrecoVenda: float = [0 for x in range(n)]
vetLucro: float = [0 for x in range(n)]
vetNome: float = [0 for x in range(n)]

for i in range(0, n):
    print(f"Produto: {i + 1}")
    vetNome[i] = input("Nome: ")
    vetPrecoCompra[i] = float(input("Preco de compra: ").replace(',', '.'))
    vetPrecoVenda[i] = float(input("Preco de venda: ").replace(',', '.'))
    print()

for i in range(0, n):
    vetLucro[i] = float(((vetPrecoVenda[i] * 100) / vetPrecoCompra[i]) - 100)

for i in range(0, n):
    if vetLucro[i] < 10:
        lucroMenor10 = lucroMenor10 + 1
    else:
        if vetLucro[i] >= 10 and vetLucro[i] < 20:
            lucroEntre10e20 = lucroEntre10e20 + 1
        else:
            lucroAcima20 = lucroAcima20 + 1

for i in range(0, n):
    valorTotalCompra = valorTotalCompra + vetPrecoCompra[i]
    valorTotalVenda = valorTotalVenda + vetPrecoVenda[i]

valorTotalLucro = valorTotalVenda - valorTotalCompra
print("RELATORIO: ")
print("Lucro abaixo de 10%: {}".format(lucroMenor10))
print("Lucro entre 10% e 20%: {}".format(lucroEntre10e20))
print("Lucro acima de 20%: {}".format(lucroAcima20))
print("Valor total de compra: {:.2f}".format(valorTotalCompra))
print("Valor total de venda: {:.2f}".format(valorTotalVenda))
print("Lucro total: {:.2f}".format(valorTotalLucro))