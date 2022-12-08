duracao: int
segundos: int
horas: int
resto: int
minutos: int

print("duração:")
duracao = int(input("Digite a duração em segundos: "))

horas = duracao // 3600
resto = duracao % 3600

minutos = resto // 60
segundos = resto % 60

print("{}:{}:{}".format(horas,minutos,segundos))