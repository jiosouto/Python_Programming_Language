# 06.Fazer um cadastro de viagem que: 
# deve pedir o nome do viajante, dar 
# as opções de destino e imprimir a selecionada.

print("Bem-vindo! Viagens Gama tem algumas ofertas para você!")
viajante = input("Digite seu nome para começarmos: ")
print("{viajante} temos 5 destinos que combinam com você:"
'''
[0] Flórida
[1] Havaí
[2] Tóquio
[3] Egito
[4] Londres''')

selecao= int(input("Selecione o número da viagem desejada: "))   #solicitação ao usuário
lista_viagem = ["Flórida", "Havaí", "Tóquio", "Egito", "Londres"]     #lista para escolha
if selecao >= 5:    #caso usuário não digite a opção correta
    print("Esta opção não está incluída em nossos destinos.")
if selecao <=4:     #verifica a seleção
     print("{} sua viagem para {} está marcada.".format(viajante,lista_viagem[selecao])) #resultado
     print("Volte sempre!")


# segunda solução (alternativa)
# print("Bem-vindo! Viagens Gama tem algumas ofertas para você!")
# viajante = input("Digite seu nome para começarmos: ")
# print("{viajante} temos 5 destinos que combinam com você:"
# '''
# [1] Flórida
# [2] Havaí
# [3] Tóquio
# [4] Egito
# [5] Londres''')

# selecao = int(input("Selecione o número da viagem desejada: "))

# if selecao == 1:
#      print("{viajante} sua viagem para a Flórida está marcada.")
# elif selecao == 2:
#     print("{viajante} sua viagem para o Havaí está marcada.")
# elif selecao == 3:
#      print("{viajante} sua viagem para Tóquio está marcada.")
# elif selecao == 4:
#      print("{viajante} sua viagem para o Egito está marcada.")
# elif selecao == 5:
#      print("{viajante} sua viagem para Londres está marcada.")
# else:
#     print("Esta opção não está incluída em nossos destinos.")
# print("Volte sempre!")