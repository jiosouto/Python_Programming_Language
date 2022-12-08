largura: float
comprimento: float
valorMetro: float
area: float
precoTerreno: float

largura = float(input("Digite a largura do terreno: ").replace(',', '.'))

comprimento = float(input("Digite o comprimento do terreno: ").replace(',', '.'))

valorMetro = float(input("Digite o valor do metro quadrado: ").replace(',', '.'))

area = largura * comprimento
precoTerreno = area * valorMetro

print("Area do terreno: = {:.2f}".format(area))
print("Preco do terreno:  = {:.2f}".format(precoTerreno))