salario: float
salarioAtualizado: float
aumento: float
porcentagem: float

print("Calcular ajuste do funcionario")
print()

salario = float(input("Digite o salrio do funcionario: ").replace(',', '.'))

if salario <= 1000:
    porcentagem = 0.20
elif salario <= 3000:
    porcentagem = 0.15

elif salario <= 8000:
    porcentagem = 0.10
else:
    print("Calcule novamente")

aumento = salario * porcentagem
salarioAtualizado = salario + aumento

print("Novo salario = {:.2f}".format(salarioAtualizado))
print("Aumento = {:.2f}".format(aumento))
print("Porcentagem = {:.0f}%".format(porcentagem * 100))