#Gabriel Reis de Brito, Kauã de Albuquerque Almeida e Lucas Randal Abreu Balderrama
def calculadora_poupanca(valor_economizado_dia):
    return valor_economizado_dia * 365

valor_economizado_dia = float(input("Digite o valor economizado por dia:  "))
economia_anual = calculadora_poupanca(valor_economizado_dia)

print(f"Será economizado no ano:  R$ {economia_anual}")