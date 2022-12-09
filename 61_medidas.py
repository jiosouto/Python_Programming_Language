A: float
B: float
C: float
areaQuadrado: float
areaTriangulo: float
areaTrapezio: float

A = float(input("Digite a medida A: ").replace(',', '.'))
B = float(input("Digite a medida B: ").replace(',', '.'))
C = float(input("Digite a medida C: ").replace(',', '.'))

areaQuadrado = A * A

areaTriangulo = (A * B) / 2

areaTrapezio = (A + B) / 2 * C

print("QUADRADO = {:.4f} ".format(areaQuadrado))
print("TRIANGULO = {:.4f} ".format(areaTriangulo))
print("TRAPEZIO = {:.4f} ".format(areaTrapezio))