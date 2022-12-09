x: int
y: int
q: str

x = int(input("Digite os valores das coordenadas x:  "))

y = int(input("Digite os valores das coordenadas y:  "))

while x != 0 or y != 0:
    if x > 0 and y > 0:
        q = "Q1"
    elif x < 0 and y > 0:
        q = "Q2"
    elif x < 0 and y < 0:
        q = "Q3"
    elif x > 0 and y < 0:
        q = "Q4"
    elif x == 0 and y == 0:
        q = "Origem"
    elif x == 0:
        q = "Eixo y"
    else:
        q = "Eixo x"

    print("QUADRANTE {}".format(q))

    x = int(input("Digite os valores das coordenadas x:  "))

    y = int(input("Digite os valores das coordenadas y:  "))