N: int
i: int
x: float
y: float
divisao: float

N = int(input("Quantos casos voce vai digitar? "))

for i in range(0, N):
    x = float(input("Entre com o numerador: ").replace(',', '.'))

    y = float(input("Entre com o denominador: ").replace(',', '.'))

    if y == 0:
        print("DIVISAO IMPOSSIVEL")
    else:
        divisao = x / y
        print("DIVISAO = {:.2f}".format(divisao))