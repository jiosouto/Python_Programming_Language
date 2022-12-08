n: int
i: int

n = int(input("Deseja a tabuada para qual valor ou digite 0 para sair?"))

while n != 0:
    for i in range(1, 11):
        print(f"{n} X {i} = {n * i}")

    n = int(input("Deseja a tabuada para qual valor ou digite 0 para sair?"))