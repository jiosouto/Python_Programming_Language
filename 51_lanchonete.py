codigo: int
quantidade: int
valorPago: float

codigo = int(input("Codigo do produto comprado: "))
quantidade = int(input("Quantidade comprada: "))

match codigo:

    case 1:
        valorPago = 5.0 * quantidade

    case 2:
        valorPago = 3.5 * quantidade
    case 3:
        valorPago = 4.8 * quantidade
    case 4:
        valorPago = 8.9 * quantidade
    case 5:
        valorPago = 7.32 * quantidade;

print("Valor a pagar: R$ {:.2f}".format(valorPago))