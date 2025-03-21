alvo = int(input('Qual número deseja buscar?: '))

def busca_sequencial(lista, alvo):
  for (index, numero) in enumerate(lista):
    if numero == alvo:
      return index
  return -1
    
lista_de_numeros = [34,213,12,45,36,98,23,3,1,9,34]
posicao_do_alvo = busca_sequencial(lista_de_numeros, alvo)

if posicao_do_alvo != -1:
  print(f'Posição do alvo {alvo} na lista: {posicao_do_alvo}')
else:
  print(f'O alvo {alvo} não se encontra na lista')