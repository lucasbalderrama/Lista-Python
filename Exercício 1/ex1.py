#Gabriel Reis de Brito, Kauã de Albuquerque Almeida e Lucas Randal Abreu Balderrama
def cidade_maior_temp(dados_temp):
    cidade_mais_quente = "" 
    maior_temperatura = 0  

    for cidade in dados_temp:
        temperatura = dados_temp[cidade]['temperatura']

        if temperatura > maior_temperatura:
            maior_temperatura = temperatura
            cidade_mais_quente = cidade

    return cidade_mais_quente

dados_cidades = {
    "Caçapava": {"temperatura": 34, "umidade": 71},
    "Taubaté": {"temperatura": 15, "umidade": 37},
    "Guarulhos": {"temperatura": 29, "umidade": 65},
    "São José dos Campos": {"temperatura": 22, "umidade": 83}
}

print("A cidade com a maior temperatura é:", cidade_maior_temp(dados_cidades))