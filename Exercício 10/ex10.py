#Gabriel Reis de Brito, Kauã de Albuquerque Almeida e Lucas Randal Abreu Balderrama
import matplotlib.pyplot as plt

def gerar_grafico_temperaturas():
    dias = ['Dia 1', 'Dia 2', 'Dia 3', 'Dia 4', 'Dia 5', 'Dia 6', 'Dia 7']
    temp_max = [32, 34, 30, 33, 31, 35, 29]
    temp_min = [20, 22, 18, 21, 19, 23, 17]

    plt.bar(dias, temp_max, color='red', label='Máximas') 
    plt.bar(dias, temp_min, color='blue', label='Mínimas', alpha=0.7)  

    plt.xlabel('Dias')
    plt.ylabel('Temperaturas (°C)')
    plt.title('Temperaturas Máximas e Mínimas dos Últimos 7 Dias')
    plt.legend() 

    plt.show()

gerar_grafico_temperaturas()
