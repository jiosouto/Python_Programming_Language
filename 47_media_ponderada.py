N: int
i: int
nota1: float
nota2: float
nota3: float
media: float

N = int(input("Quantos casos voce vai digitar? "))

for i in range(0, N):
    print("Digite tres numeros: ")
    nota1 = float(input().replace(',', '.'))
    nota2 = float(input().replace(',', '.'))
    nota3 = float(input().replace(',', '.'))

    media = float(((nota1 * 2) + (nota2 * 3) + (nota3 * 5)) / (2 + 3 + 5))
    print("MEDIA = {:.1f}".format(media))