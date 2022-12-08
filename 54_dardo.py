d1: float
d2: float
d3: float
maior: float

print("Digite as tres distancias:")
d1 = float(input().replace(',', '.'))
d2 = float(input().replace(',', '.'))
d3 = float(input().replace(',', '.'))

if d1 > d2 and d1 > d3:

    maior = d1

elif d2 > d3:

    maior = d2

else:

    maior = d3

print("MAIOR DISTANCIA = {:.2f}".format(maior))