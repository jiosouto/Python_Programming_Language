import math

base: float
altura: float
area: float
perimetro: float
diagonal: float

base = float(input("Digite a base do retangulo: ").replace(',', '.'))
altura = float(input("Digite altura do retangulo: ").replace(',', '.'))

area = base * altura;
perimetro = 2 * (base + altura);
diagonal = math.sqrt(math.pow(base, 2) + math.pow(altura, 2));

print("Area:  {:.4f}".format(area))
print("Perimetro:  {:.4f}".format(perimetro))
print("Diagonal:  {:.4f}".format(diagonal))