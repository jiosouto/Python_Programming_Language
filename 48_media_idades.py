idade: int
soma: int
cont: int
media: float

soma = 0;
cont = 0;

idade = int(input("Digite as idades: "))

while idade >= 0:
    soma = soma + idade
    cont = cont + 1
    idade = int(input("Digite as idades: "))
if cont == 0:
    print("IMPOSSIVEL CALCULAR")
else:
    media = float(soma / cont)
    print("MEDIA = {:.2f}".format(media))