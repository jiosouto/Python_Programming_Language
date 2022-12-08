precoProduto: float
quantidade: float
pagamento: float
troco: float

print("Caixa:")
precoProduto = float(input("Preco unitário do produto: ").replace(',', '.'))
quantidade = float(input("Quantidade comprada: ").replace(',', '.'))
pagamento = float(input("Dinheiro recebido: ").replace(',', '.'))

troco = pagamento - precoProduto * quantidade

print("troco = R$ {:.2f} ".format(troco))