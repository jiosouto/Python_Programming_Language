x: int
y: int
soma: int
i: int
troca: int

print("Digite dois numeros ou dua vezes o zero para finalizar: ")
x = int(input())
y = int(input())

while x != 0 or y != 0:
    i = 0
    soma = 0

    if x > y:
        troca = x
        x = y
        y = troca

    for i in range(x + 1, y):
        if i % 2 != 0:
            soma = soma + i

    print("Soma dos impare = {}".format(soma))
    soma = 0;
    print("Digite dois numeros ou dua vezes o zero para finalizar: ")
    x = int(input())
    y = int(input())