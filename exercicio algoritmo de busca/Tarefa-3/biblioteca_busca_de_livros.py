# # A biblioteca de uma escola possui uma lista de livros, onde cada livro tem um ID e um Título.
# # Seu objetivo é implementar dois métodos para buscar um livro pelo ID:

#   1. Busca Sequencial (para listas desordenadas)
#   2. Busca Binária (para listas ordenadas)

# Passos para resolver o exercício:
#   1. Criar uma lista com alguns livros (cada livro com um ID e um título).
#   2. Implementar a função busca_sequencial(lista, id_procurado).
#   3. Implementar a função busca_binaria(lista, id_procurado) (garantindo que a lista esteja
#   ordenada pelo ID).
#   4. Testar ambas as funções buscando um livro específico.

livros = [
  {"id": 105, "titulo": "O Senhor dos Anéis"},
  {"id": 210, "titulo": "1984"},
  {"id": 157, "titulo": "Dom Casmurro"},
  {"id": 332, "titulo": "O Pequeno Príncipe"},
  {"id": 190, "titulo": "Harry Potter"},
]

def busca_sequencial(lista, id_procurado):
  for livro in lista:
    if livro["id"] == id_procurado:
      return livro
  return -1


lista_ordenada = sorted(livros, key=lambda x: x["id"]) # Lista ordenada

def busca_binaria(lista, id_procurado):
  pos_inicial = 0
  pos_final = len(lista) -1

  while pos_inicial <= pos_final:
    pos_meio = (pos_inicial + pos_final) // 2

    if lista[pos_meio]["id"] == id_procurado:
      return lista[pos_meio]
    if lista[pos_meio] > id_procurado:
      pos_final = pos_meio - 1
    else:
      pos_inicial = pos_meio + 1

  return -1

resultado_bs = busca_sequencial(livros, 190)
resultado_bb = busca_binaria(lista_ordenada, 190)

print(resultado_bs)
print(resultado_bb)