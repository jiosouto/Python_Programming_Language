x: int
y: int
ordem: str

x = int(input("Digite o primeiro numero:  "))

y = int(input("Digite o segundo numero:  "))

while x != y:
    if x > y:
        ordem = "Decrescente"
    else:
        ordem = "Crescente"

    print(f"A ordem de {x} e {y} eh: {ordem}")

    x = int(input("Digite o primeiro numero:  "))
    y = int(input("Digite o segundo numero:  "))