alvo = int(input('Qual número deseja buscar?: '))
tamanho_da_lista = int(input('Quer procurar em uma lista de quantos numeros? '))

lista_de_numeros = []

for numero in range(1, tamanho_da_lista):
  lista_de_numeros.append(numero)

def busca_sequencial(lista, alvo):
  for (index, numero) in enumerate(lista):
    if numero == alvo:
      return index
  return -1
    

posicao_do_alvo = busca_sequencial(lista_de_numeros, alvo)

if posicao_do_alvo != -1:
  print(f'Posição do alvo {alvo} na lista é: {posicao_do_alvo}')
else:
  print(f'O alvo {alvo} não se encontra na lista')