#Gabriel Reis de Brito, Kauã de Albuquerque Almeida e Lucas Randal Abreu Balderrama
def calcula_media_temperatura(temperaturas):
    return sum(temperaturas) / len(temperaturas)

# Dados fictícios de temperaturas (em °C) para 5 cidades:
temperaturas_cidades = {
    "São José dos Campos": [23.5, 25.1, 22.8, 24.0, 23.9],
    "Guarulhos": [18.2, 19.0, 18.5, 19.2, 18.8],
    "Taúbate": [30.1, 31.0, 29.5, 30.8, 31.2],
    "São José do rio preto": [15.0, 14.8, 15.5, 14.9, 15.2],
    "Caçapava": [27.8, 28.3, 27.5, 28.1, 27.9]
}

for cidade, temperaturas in temperaturas_cidades.items():
    media = calcula_media_temperatura(temperaturas)
    print(f"Média de temperaturas de {cidade}: {media:.2f}°C")
