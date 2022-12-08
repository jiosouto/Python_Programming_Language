horaInicial: int
horaFinal: int
duracao: int

horaInicial = int(input("Hora inicial: "))
horaFinal = int(input("Hora final: "))

if horaInicial < horaFinal:
    duracao = horaFinal - horaInicial

else:
    duracao = 24 - horaInicial + horaFinal

print("O JOGO DUROU {} HORA(S)".format(duracao))