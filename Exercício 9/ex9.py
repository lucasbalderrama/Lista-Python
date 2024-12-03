#Gabriel Reis de Brito, Kauâ de Albuquerque Almeida e Lucas Randal Abreu Balderrama

lista_medidas = []
desastres= ["Tremor de terra", "Tsunami", "Deslizamento de terra", "Ciclone", "Tempestade", "Onda de calor"]

for i in desastres:
    medida = int(input(f"Insira a medida do desastre '{i}': "))
    lista_medidas.append(medida)

if lista_medidas[0] < 3.9:
    print("")
elif lista_medidas[0] > 6 and lista_medidas[0] < 6.9:
    print("")
elif lista_medidas[0] > 7:
    print("")

if lista_medidas[1] < 2:
    print("")
elif lista_medidas[1] > 2 and lista_medidas[1] < 5:
    print("")
elif lista_medidas[1] > 5:
    print("")

if lista_medidas[2] < 3.9:
    print("")
elif lista_medidas[2] > 6 and lista_medidas[2] < 6.9:
    print("")
elif lista_medidas[2] > 7:
    print("")

if lista_medidas[3] < 3.9:
    print("")
elif lista_medidas[3] > 6 and lista_medidas[3] < 6.9:
    print("")
elif lista_medidas[3] > 7:
    print("")

if lista_medidas[4] < 3.9:
    print("")
elif lista_medidas[4] > 6 and lista_medidas[4] < 6.9:
    print("")
elif lista_medidas[4] > 7:
    print("")

if lista_medidas[5] < 3.9:
    print("")
elif lista_medidas[5] > 6 and lista_medidas[5] < 6.9:
    print("")
elif lista_medidas[5] > 7:
    print("")