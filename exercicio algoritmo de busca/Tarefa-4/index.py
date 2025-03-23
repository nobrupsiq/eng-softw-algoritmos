# Tarefa 4 – Desafio
# 1. Gere uma lista com 1.000.000 de números aleatórios e compare os tempos de
# execução. ✔️
# 2. Modifique o programa para contar quantas comparações cada método realiza. ✔️
# 3. Peça ao usuário para inserir vários números e armazene as buscas em um histórico.

import random
import time

lista_de_numeros = []
historico_do_usuario = []

numeros_aleatorios = random.sample(range(1, 1000001), 1000000)

for numero in numeros_aleatorios:
  lista_de_numeros.append(numero)

contador_de_comparacao_busca_sequencial = 0
def busca_sequencial(lista, numero):
  global contador_de_comparacao_busca_sequencial
  for index in lista:
    contador_de_comparacao_busca_sequencial += 1
    if index == numero:
      return index
  return -1

lista_ordenada = sorted(lista_de_numeros)

contador_de_comparacao_busca_binaria = 0
def busca_binaria(lista, numero):
  global contador_de_comparacao_busca_binaria
  pos_inicial = 0
  pos_final = len(lista) -1

  while pos_inicial <= pos_final:
    pos_meio = (pos_inicial + pos_final) // 2
    contador_de_comparacao_busca_binaria += 1

    if lista[pos_meio] == numero:
      return lista[pos_meio]
    if lista[pos_meio] > numero:
      pos_final = pos_meio -1
    else:
      pos_inicial = pos_meio + 1
  return -1

inicio_tempo_busca_sequencial = time.time()
resultado_busca_sequencial = busca_sequencial(lista_de_numeros, 7)
tempo_final_busca_sequencial = time.time() - inicio_tempo_busca_sequencial
print(f'BUSCA SEQUENCIAL -> demorou: {tempo_final_busca_sequencial:.6f} segundos para encontrar o numero {resultado_busca_sequencial} e fez {contador_de_comparacao_busca_sequencial} comparações')

inicio_tempo_busca_binaria = time.time()
resultado_busca_binaria = busca_binaria(lista_ordenada, 7)
tempo_final_busca_binaria = time.time() - inicio_tempo_busca_binaria
print(f'BUSCA BINARIA -> demorou: {tempo_final_busca_binaria:.6f} segundos para encontrar o numero {resultado_busca_binaria} e fez {contador_de_comparacao_busca_binaria} comparações')

# Eu percebi que para as listas pequenas a busca sequencial é mais eficiente, com uma lista de 20 numeros a lista sequencial foi uns 000004 segundos mais rapida que a busca binaria.

# Ja com a lista com 1 milhao de numeros a busca binaria deu nocaute na busca sequencial, diferença gigante! Então cheguei a conclusão que a busca binaria ela escala bem melhor com listas relativamente maiores.
