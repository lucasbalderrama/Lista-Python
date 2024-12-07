#Gabriel Reis de Brito, Kauã de Albuquerque Almeida e Lucas Randal Abreu Balderrama
def filtra_eventos(eventos):
    return [evento for evento in eventos if evento['intensidade'] > 7]

eventos = [
    {"catástrofe": "enchente", "intensidade": 6},
    {"catástrofe": "furacão", "intensidade": 8},
    {"catástrofe": "terremoto", "intensidade": 9}
]

eventos_filtrados = filtra_eventos(eventos)
print(eventos_filtrados) 