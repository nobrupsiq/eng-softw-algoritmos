# Escreva uma função recursiva que calcule a potência de um número x elevado a um
# expoente n.

def calcularPotencia(base, expoente):
  if expoente == 0:
    return 1
  
  return base * calcularPotencia(base, expoente - 1)

resultado = calcularPotencia(3, 3)
print(resultado)


