# Para a parte 4 etapa que pede ao usuario para guardar o historico, primeiro vou criar uma função para guardar a busca do usuario e uma outra função para exibir o historico
import random
import time

lista_de_numeros = []
historico_do_usuario = []

numeros_aleatorios = random.sample(range(1, 1000001), 1000000)
for numero in numeros_aleatorios:
  lista_de_numeros.append(numero)

# BUSCA SEQUENCIAL
contador_de_comparacao_busca_sequencial = 0
def busca_sequencial(lista, numero):
  global contador_de_comparacao_busca_sequencial
  for index in lista:
    contador_de_comparacao_busca_sequencial += 1
    if index == numero:
      return index
  return -1

# BUSCA BINARIA
lista_de_numeros_ordenada = sorted(lista_de_numeros) # Lista ordenada

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

# ARMAZENAR HISTORICO DO USUARIO
def guardar_busca_do_usuario(numero, funcao, comparacoes, tempo):
  historico_do_usuario.append(
    {
      "numero_procurado": numero,
      "funcao": funcao,
      "comparacoes": comparacoes,
      "tempo": tempo
    }
  )

# EXIBIR O HISTORICO DE BUSCA DO USUARIO
def exibir_hitorico_de_busca_do_usuario():
  if not historico_do_usuario:
    print("\nHistorico de busca vazio!")
  for busca in historico_do_usuario:
    print(f"Numero de busca: {busca["numero_procurado"]} | Função utilizada: {busca["funcao"]} | Comparações: {busca["comparacoes"]} | Tempo: {busca["tempo"]:.6f} segundos")

while True:
  print("""
        ---- Escolha uma opção ----  
        
            1 - Busca sequencial
            2 - Busca binaria
            3 - Exibir historico de busca
            4 - Sair
  """)

  opcao = input("Opcao: ")
  if opcao == '1' or opcao == '2':
    escolha_do_numero = int(input("Numero a ser encontrado: "))
    
    if opcao == '1':
      inicio_tempo_busca_sequencial = time.time()
      resultado_busca_sequencial = busca_sequencial(lista_de_numeros, escolha_do_numero)
      tempo_final_busca_sequencial = time.time() - inicio_tempo_busca_sequencial
      print(f'BUSCA SEQUENCIAL -> demorou: {tempo_final_busca_sequencial:.6f} segundos para encontrar o numero {resultado_busca_sequencial} e fez {contador_de_comparacao_busca_sequencial} comparações')
      guardar_busca_do_usuario(escolha_do_numero, "Busca sequencial", contador_de_comparacao_busca_sequencial, tempo_final_busca_sequencial)
      # Quebrei a cabeça aqui, se eu não zerar o contador apos buscar um numero, ele fica acumulando infinito
      contador_de_comparacao_busca_sequencial = 0

    elif opcao == "2":
      inicio_tempo_busca_binaria = time.time()
      resultado_busca_binaria = busca_binaria(lista_de_numeros_ordenada, escolha_do_numero)
      tempo_final_busca_binaria = time.time() - inicio_tempo_busca_binaria
      print(f'BUSCA BINARIA -> demorou: {tempo_final_busca_binaria:.6f} segundos para encontrar o numero {resultado_busca_binaria} e fez {contador_de_comparacao_busca_binaria} comparações')
      guardar_busca_do_usuario(escolha_do_numero, "Busca binaria", contador_de_comparacao_busca_binaria, tempo_final_busca_binaria)
      contador_de_comparacao_busca_binaria = 0

  elif opcao == "3":
    exibir_hitorico_de_busca_do_usuario()

  elif opcao == "4":
    print("Saindo do programa!")
    break
  else:
    print("Opção invalida! Vamos de novo.")