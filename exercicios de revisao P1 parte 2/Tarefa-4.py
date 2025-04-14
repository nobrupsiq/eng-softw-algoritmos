# Um número é considerado perfeito quando a soma de seus divisores (excluindo ele mesmo) é
# igual ao próprio número. Exemplo: 28 → 1 + 2 + 4 + 7 + 14 = 28.
# Crie um programa que solicite um número inteiro positivo e diga se ele é perfeito ou não

def verificador_de_numero_perfeito(numero):
  divisores = []
  for index in range(1, numero):
    if numero % index == 0:
      divisores.append(index)
  if sum(divisores) == numero:
    print('Número perfeito!')
  else:
    print('Número não perfeito!')
  return divisores

user_numero = int(input('Digite um número inteiro: '))
verificador_de_numero_perfeito(user_numero)
