#Gabriel Reis de Brito, Kauã de Albuquerque Almeida e Lucas Randal Abreu Balderrama
def converter_temperatura(celsius):
    fahrenheit = (celsius * 9/5) + 32
    kelvin = celsius + 273.15
    return fahrenheit, kelvin

#exemplo de uso:
celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit, kelvin = converter_temperatura(celsius)
print(f"{celsius}°C equivalem a {fahrenheit:.2f}°F e {kelvin:.2f}K.")
