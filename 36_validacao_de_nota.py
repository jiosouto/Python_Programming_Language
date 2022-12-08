nota1: float
nota2: float
media: float

nota1 = float(input("Digite a primeira nota: ").replace(',', '.'))

while nota1 < 0 or nota1 > 10:
    nota1 = float(input("Valor invalido! Tente novamente: ").replace(',', '.'))

nota2 = float(input("Digite a segunda nota: ").replace(',', '.'))

while nota2 < 0 or nota2 > 10:
    nota2 = float(input("Valor invalido! Tente novamente: ").replace(',', '.'))

media = float((nota1 + nota2) / 2)
print("MEDIA = {:.2f}".format(media))