import math

a: float
b: float
c: float
x1: float
x2: float
delta: float

a = float(input("Coeficiente a: ").replace(',', '.'))

b = float(input("Coeficiente b: ").replace(',', '.'))

c = float(input("Coeficiente c: ").replace(',', '.'))

delta = math.pow(b, 2) - (4 * a * c)

if a == 0 or delta < 0:
    print("Esta equacao nao possui raizes reais")

else:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)

    print("X1 = {:.4f} ".format(x1))
    print("X2 = {:.4f} ".format(x2))