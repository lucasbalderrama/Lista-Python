def classificar_impacto(medida, limites):
    if medida < limites[0]:
        return "Impacto: Leve"
    elif limites[0] <= medida <= limites[1]:
        return "Impacto: Moderado"
    else:
        return "Impacto: Alto"

desastres = ["Tremor de terra", "Tsunami", "Deslizamento de terra", 
             "Ciclone", "Tempestade", "Onda de calor"]

limites = [
    [3.9, 6.9],
    [2, 5],
    [10000, 100000],
    [153, 208],
    [50, 100],
    [38, 42]
]

print(f"""Medidas: 
      {desastres[0]}: Escala Ritcher; 
      {desastres[1]}: Altura da onda (m);
      {desastres[2]}: Volume de material deslocado (m³);
      {desastres[3]}: Velocidade dos ventos (km/h);
      {desastres[4]}: Volume da chuva (mm);
      {desastres[5]}: Temperatura máxima (°C).\n""")

lista_medidas = []
for desastre in desastres:
    medida = float(input(f"Insira a medida do desastre '{desastre}': "))
    lista_medidas.append(medida)

print("<-------------------------------->") # Apenas uma quebra de linha

for i, medida in enumerate(lista_medidas):
    impacto = classificar_impacto(medida, limites[i])
    print(f"{desastres[i]} - {impacto}")