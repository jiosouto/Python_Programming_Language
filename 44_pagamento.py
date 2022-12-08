nome: str
valorHora: float
pagamento: float
horasTrabalhadas: int

nome = input("Nome: ")
valorHora = float(input("Valor por hora: ").replace(',', '.'))

horasTrabalhadas = int(input("Horas trabalhadas: "))

pagamento = float(valorHora * horasTrabalhadas)

print("O pagamento para {} deve ser R$ {:.2f}".format(nome,pagamento))