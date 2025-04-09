# Conversor de Temperatura
# Crie um programa em Python que solicite ao usuário uma temperatura em graus Celsius e
# converta para Fahrenheit e Kelvin. O sistema deve utilizar funções para cada conversão:
#   • Fahrenheit = (C × 9/5) + 32
#   • Kelvin = C + 273.15
# Ao final, exiba os três valores: Celsius, Fahrenheit e Kelvin.

temperatura_celsius = float(input('Temperatura em Celsius: '))


def fahrenheit(celcius):
    return (celcius * 9/5) + 32

def kelvin(celcius):
    return celcius + 273.15

fahren = fahrenheit(temperatura_celsius)
kelv = kelvin(temperatura_celsius)

print(f'Celsius: {temperatura_celsius} | Fahrenheit: {fahren} | Kelvin: {kelv}')


