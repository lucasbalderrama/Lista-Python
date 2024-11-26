#Gabriel Reis de Brito, Kauã de Albuquerque Almeida e Lucas Randal Abreu Balderrama
import statistics

def calcular_estatisticas(niveis):
    media = sum(niveis) / len(niveis)
    mediana = statistics.median(niveis)
    return media, mediana

# Dados fictícios do nível do rio em Caçapava (em metros):
dados_mensais = [2.5, 2.8, 3.0, 2.6, 3.1, 2.9, 2.7, 3.3, 2.4, 3.0, 2.8, 2.7]

media, mediana = calcular_estatisticas(dados_mensais)
print(f"Média do nível do rio: {media:.2f} metros")
print(f"Mediana do nível do rio: {mediana:.2f} metros")
