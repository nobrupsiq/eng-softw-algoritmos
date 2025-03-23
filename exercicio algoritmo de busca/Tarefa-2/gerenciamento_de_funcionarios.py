# 1. Cenário 1: A lista de funcionários não está ordenada.

import random
import string
import time

funcionarios = []

def gerar_nome():
    letras = string.ascii_lowercase
    nome = ''.join(random.choices(letras, k=5))  # Nome de 5 letras
    sobrenome = ''.join(random.choices(letras, k=7))  # Sobrenome de 7 letras
    return nome.capitalize() + " " + sobrenome.capitalize()

id_aleatorio = random.sample(range(1, 100001), 100000)

for identificador in id_aleatorio:
    funcionario = {
        "id": identificador,
        "nome": gerar_nome()
    }

    funcionarios.append(funcionario)

def busca_sequencial(lista, id):
    for index in lista:
        if index["id"] == id:
            return index
    return -1


# 2. Cenário 2: A lista de funcionários está ordenada pelo ID

lista_funcionarios_ordenada = sorted(funcionarios, key=lambda x: x["id"]) # Interessante essa função anonima do sorted, não conhecia, eu nao estava conseguindo ordenar a lista pelo ID. O sorted não estava encontrando um numero ou uma letra para ordenar, o key=lambda diz que para cada funcionario['id'] eu vou ordenar, serve como um direcionamento para o ID. Cada erro é uma oportunidade de aprender algo novo.

def busca_binaria(lista, id):
  pos_inicial = 0
  pos_final = len(lista) -1

  while pos_inicial <= pos_final:
    pos_meio = (pos_inicial + pos_final) // 2

    if lista[pos_meio]["id"] == id:
      return lista[pos_meio]
    if lista[pos_meio]["id"] > id:
      pos_final = pos_meio -1
    else:
      pos_inicial = pos_meio + 1
  return -1

# TEMPO DA BUSCA NÃO ORDENADA COM BUSCA SEQUENCIAL
inicio = time.time()
resultado_busca_sequencial = busca_sequencial(funcionarios, 67)
tempo_da_busca_sequencial = time.time() - inicio

# TEMPO DA BUSCA ORDENADA COM BUSCA BINARIA
inicio = time.time()
resultado_busca_binaria = busca_binaria(lista_funcionarios_ordenada, 67)
tempo_da_busca_binaria = time.time() - inicio

print(f'Busca sequencial encontrou: {resultado_busca_sequencial} em {tempo_da_busca_sequencial:.6f} segundos')
print(f'Busca Binaria encontrou: {resultado_busca_binaria} em {tempo_da_busca_binaria:.6f} segundos')




