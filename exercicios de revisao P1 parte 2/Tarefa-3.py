# Implemente um programa para gerenciar o estoque de uma pequena loja. O sistema deve
# permitir:
#   1. Adicionar um novo produto com nome e quantidade.
#   2. Listar todos os produtos com suas respectivas quantidades.
#   3. Atualizar o estoque de um produto (aumentar ou reduzir quantidade).
#   4. Remover um produto do sistema.
# Utilize dicionários para armazenar os dados.

import time

estoque = {}

def adicionar_produto(nome, quantidade):
  estoque[nome] = {}
  estoque[nome]["Quantidade"] = quantidade
  return nome, quantidade

def listar_produtos():
  for produto, dados in estoque.items():
    print(f'Nome do produto: {produto} | Quantidade em estoque: {dados['Quantidade']}')

def atualizar_quantidade(nome, nova_quantidade):
  estoque[nome]['Quantidade'] = nova_quantidade
  return nome, nova_quantidade

def remover_produto(nome):
    del estoque[nome]
    print('Produto removido com sucesso!')
    return nome

while True:
  print("""
    ---- Sistema de estoque ----\n
         1. Adicionar produto
         2. Listar todos os produtos
         3. Atualizar quantidade de um produto
         4. Remover produto
         5. Sair
""")
  opcao = input('Opcao: ')

  if opcao == '1':
    nome = input('Nome do produto: ').capitalize() # Sempre a primeira letra do nome maiuscula
    if nome not in estoque:
      quantidade = int(input('Quantidade de estoque: '))
      adicionar_produto(nome, quantidade)
      print("\nAdicionando produto ao estoque... ⌛")
      time.sleep(2)
      print("Produto adicionado com sucesso! ✔️")
    else:
      print(f'\nO produto "{nome}" já está incluido no estoque.')
  elif opcao == '2':
    if len(estoque) > 0:
      print('\nBuscando produtos... ⌛')
      time.sleep(2)
      listar_produtos()
    else:
      print('\nBuscando produtos... ⌛')
      time.sleep(2)
      print('Estoque vazio!')
  elif opcao == '3':
    nome = input('Nome do produto: ').capitalize()
    if nome not in estoque:
      print('\nVerificando estoque...⌛')
      time.sleep(2)
      print(f'O produto "{nome}" não existe no estoque!')
    else:
     nova_quantidade = int(input('Nova quantidade em estoque: '))
     atualizar_quantidade(nome, nova_quantidade)
     print('\nAtualizando o estoque! Aguarde...⌛')
     time.sleep(2)
     print('Estoque atualizado com sucesso! ✔️')
  elif opcao == '4':
      nome = input('Nome do produto: ').capitalize()
      if nome not in estoque:
        print('\nBuscando produto no estoque...⌛')
        time.sleep(2)
        print(f'O produto "{nome}" não existe no estoque!')
      else:
        remover_produto(nome)
        print('\nBuscando produto no estoque...⌛')
        time.sleep(2)
        print(f'O produto "{nome}" foi removido com sucesso! ✔️')
  elif opcao == '5':
    print('Saindo...')
    break
  else:
    print('\nOps! Parece que você digitou algo errado, vamos de novo!')