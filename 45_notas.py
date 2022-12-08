nota1: float
nota2: float
notaFinal: float

nota1 = float(input("Digite a primeira nota: ").replace(',', '.'))
nota2 = float(input("Digite a segunda nota: ").replace(',', '.'))

notaFinal = nota1 + nota2;

print("NOTA FINAL =  {:.1f} ".format(notaFinal))

if notaFinal < 60.0:
    print("REPROVADO")

else:
    print("APROVADO")