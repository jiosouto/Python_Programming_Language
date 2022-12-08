preco: float
dinheiro: float
troco: float
resto: float
quantidade: int

preco = float(input("Preco unitario do produto: ").replace(',', '.'))

quantidade = int(input("Quantidade comprada: "))

dinheiro = float(input("Dinheiro recebido: ").replace(',', '.'))

if dinheiro >= (preco * quantidade):
    troco = float(dinheiro - preco * quantidade)
    print("TROCO = {:.2f}".format(troco))

else:
    resto = preco * quantidade - dinheiro
    print("DINHEIRO INSUFICIENTE. FALTAM {:.2f} REAIS".format(resto))