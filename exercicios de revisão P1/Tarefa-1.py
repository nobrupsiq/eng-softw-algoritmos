import math

raio = float(input('Raio da esfera: '))

def calculo_volume_de_esfera(raio):
  volume = 4/3 * math.pi * math.pow(raio, 3)
  return f"Volume da esfera: {volume}"

resultado = calculo_volume_de_esfera(raio)
print(resultado)