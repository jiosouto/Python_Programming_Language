# 01.Elabore um algoritmo em Python que receba um número 
# inteiro e escreva na tela o número fornecido, o antecessor 
# desse número e o sucessor desse número;.

numero = int(input("Digite um número: "))   #solicita número ao usuário
print("Seu número foi {}".format(numero))   #numero digitado pelo usuário
numero -= 1 #operação antesessor n - 1
print("O antessor é {}".format(numero))
numero += 2 #operação sucessor (n - 1) + 1
print("O sucessor é {}".format(numero))