#Gabriel Reis de Brito, Kauâ de Albuquerque Almeida e Lucas Randal Abreu Balderrama
import pandas as pd

ler = pd.read_csv(r"C:\Users\Gabriel\Documents\Lista-Python\Exercício 8\temperaturas.csv")

media_janeiro = ler["Janeiro"].mean()
media_fevereiro = ler["Fevereiro"].mean()
media_marco = ler["Março"].mean()

print("<- Média de temperaturas ->")
print(f"Janeiro: {media_janeiro:.1f}°C \nFevereiro: {media_fevereiro:.1f}°C \nMarço: {media_marco:.1f}°C")