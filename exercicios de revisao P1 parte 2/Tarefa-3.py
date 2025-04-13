# Implemente um programa para gerenciar o estoque de uma pequena loja. O sistema deve
# permitir:
#   1. Adicionar um novo produto com nome e quantidade.
#   2. Listar todos os produtos com suas respectivas quantidades.
#   3. Atualizar o estoque de um produto (aumentar ou reduzir quantidade).
#   4. Remover um produto do sistema.
# Utilize dicionários para armazenar os dados.

estoque = {}

def adicionar_produto(nome, quantidade):
  estoque[nome] = {}
  estoque[nome]['Quantidade'] = quantidade
  return nome, quantidade

def listar_produtos():
  for nome, dados in estoque.items():
    print(f'Nome do produto: {nome} | Quantidade em estoque: {dados['Quantidade']}')

def atualizar_estoque(nome, nova_quantidade):
  estoque[nome]['Quantidade'] = nova_quantidade
  return nome, nova_quantidade

def remover_produto(nome):
  estoque.pop(nome)
  return nome

adicionar_produto('Colher', 22)
adicionar_produto('Garfo', 31)
remover_produto('Colher')
listar_produtos()