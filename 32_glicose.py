glicose: float
classificacao: str

glicose = float(input("Digite a medida da glicose: ").replace(',', '.'))

if glicose <= 100:
    classificacao = "Normal"

elif glicose <= 140:
    classificacao = "Elevado"

else:
    classificacao = "Diabetes"

print("Classificacao: {}".format(classificacao))