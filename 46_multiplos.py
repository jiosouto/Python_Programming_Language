x: int
y: int

print("Digite dois numeros inteiros:")
x = int(input())
y = int(input())

if x % y == 0 or y % x == 0:
    print("Sao multiplos")
else:
    print("Nao sao multiplos")