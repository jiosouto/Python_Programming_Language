mediaIdade: float
idade1: int
idade2: int
nome1: str
nome2: str

print("Dados da primeira pessoa: ")
nome1 = input("Nome: ")
idade1 = int(input("idade: "))

print("Dados da segunda pessoa:")
nome2 = input("Nome: ")
idade2 = int(input("idade: "))

mediaIdade = float((idade1 + idade2) / 2.0)

print("A idade media de {} e {} eh de {:.1f} anos".format(nome1,nome2,mediaIdade))