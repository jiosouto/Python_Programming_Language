# 15.Fazer um sistema de compras que:
# mostre um dicionário com os objetos (Nome, Preço e Cor), 
# pedir o nome do usuário e fazer com o que o 
# usuário selecione um objeto e imprimir a compra na tela.

#Solicita o nome do usuário
nome = input("Bem-vindo a nossa loja! Digite seu nome para começarmos: \n")
#dicionario com as opções de compra
dicionario_compras = {"Nome": "Blusa P","Preço": "R$29,90","Cor":"Azul"}, {"Nome": "Camiseta M","Preço": "R$39,90","Cor": "Florida"}, {"Nome": "Short M","Preço": "R$59,90","Cor": "Verde"}
#loop infinito
while True:
        contador = 0    #índice
        for lista in dicionario_compras:        #lista as opções comppras
                print("{} - {}".format(contador,lista))  #Imprime as opções comppras
                contador += 1   #incremento
        #imprime desistência de compra, fim do loop
        print("\nSe desistiu da compra, digite {} para sair!\n".format(contador))       
        #solicita opção de compra
        compra = int(input("{} digite o número da sua opção de compra: \n").format(nome))
        if compra == 0:         #condição produto 1
                print("{} parabéns! Você acaba de adquirir uma Blusa P\n".format(nome))
        elif compra == 1:       #condição produto 2
                print("{} parabéns! Você acaba de adquirir uma Camiseta M\n".format(nome))
        elif compra == 2:       #condição produto 3
                print("{} parabéns! Você acaba de adquirir uma Camiseta M\n".format(nome))
        elif compra == 3:       #condição sair da compra
                print("{} volte sempre!".format(nome))
                break   #fim do loop
        elif compra >= 4:       ##condição opção de compra errada
                print("{} a opção não existe".format(nome))