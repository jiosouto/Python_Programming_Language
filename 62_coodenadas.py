X: float
Y: float

X = float(input("Valor de X: ").replace(',', '.'))
Y = float(input("Valor de Y: ").replace(',', '.'))

if X > 0 and Y > 0:
    print("Q1")

elif X < 0 and Y > 0:
    print("Q2")

elif X < 0 and Y < 0:
    print("Q3")

elif X > 0 and Y < 0:
    print("Q4")

elif X == 0 and Y == 0:
    print("Origem")

elif X == 0:
    print("Eixo Y")

else:
    print("Eixo X")