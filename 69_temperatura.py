temperatura: float
temperaturaConvertida: float
unidadeMedida: str
unidadeMedidaResposta: str
unidadeResposta: str

unidadeMedida = input("Voce vai digitar a temperatura em qual escala (C/F)? ")

if unidadeMedida == 'F' or unidadeMedida == 'f':
    temperatura = float(input("Digite a temperatura em Fahrenheit: ").replace(',', '.'))
    temperaturaConvertida = (5.0 / 9.0) * (temperatura - 32.0)
    unidadeResposta = "celsius"
    unidadeMedidaResposta = 'C'

elif unidadeMedida == 'C' or unidadeMedida == 'c':
    temperatura = float(input("Digite a temperatura em Celsius: ").replace(',', '.'))
    temperaturaConvertida = temperatura * 1.8 + 32
    unidadeResposta = "fahrenheit"
    unidadeMedidaResposta = 'F'

else:
    unidadeResposta = "Conversão impossivel para unidade informada"

if unidadeResposta == "Conversão impossivel para unidade informada":

    print(unidadeResposta)

else:
    print("Temperatura equivalente em {}: {:.2f} °{}".format(unidadeResposta,temperaturaConvertida,unidadeMedidaResposta))