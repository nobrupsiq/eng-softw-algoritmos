# Escreva uma função recursiva que calcule a soma dos dígitos de um número inteiro
# positivo.

def calculo(numero):
  if len(str(numero)) == 1:
    return numero
  
  return numero % 10 + calculo(numero // 10)

resultado = calculo(197)
print(resultado)
