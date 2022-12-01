# 02.Algoritmo para calcular a média do aluno que:
# deve colocar o nome do aluno, colocar 4 notas
# e imprimir sua média.

# solicita nome do aluno
aluno = input("Digite o nome do aluno: ")

# solicita notas do aluno
num1 = float(input("Digite a primeira nota: "))
num2 = float(input("Digite a segunda nota: "))
num3 = float(input("Digite a terceira nota: "))
num4 = float(input("Digite a quarta nota: "))

media = (num1 + num2 + num3 + num4)/4 #executa operação matemática
print("A nota média do aluno {} é {:0.1f}".format(aluno,media)) #imprime resultado