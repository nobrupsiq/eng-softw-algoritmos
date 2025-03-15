# Etapa 3 – Reescreva o código da Etapa1 com dicionários

estoque_dicionarios = {}

def adicionar_produto(nome, preco, quantidade):
  produto = {
    'preco': preco,
    'quantidade': quantidade
  }
  estoque_dicionarios[nome.capitalize()] = produto
  print('Produto adicionado com sucesso!')

def listar_produtos():
  for index, (nome, valor) in enumerate(estoque_dicionarios.items()):
    print(f'{index + 1}. Nome: {nome} | Preço: {valor['preco']:.1f} | Quantidade: {valor['quantidade']}')

def atualizar_quantidade(nome, quantidade):
  for produto, valor in estoque_dicionarios.items():
    if produto == nome.capitalize(): 
      valor['quantidade'] = quantidade
      print('Quantidade atualizada com sucesso!')

def remover_produto(nome):
  # Precisei criar uma lista para armazenar as chaves do meu dicionario que no caso é o nome do produto. Criei isso porque eu não estava conseguindo remover o produto iterando pelo dicionario, quando eu faço uma iteração pelo dicionario e removo o item encontrado, me retorna um erro dizendo que o tamanho do dicionario foi modificado e entao encerra o looping.
  chaves_para_remover = []

  for produto in estoque_dicionarios:
    if produto == nome.capitalize():
      chaves_para_remover.append(produto)
  
  for chave in chaves_para_remover:
    estoque_dicionarios.pop(chave)
    print('Produto removido com sucesso!')


adicionar_produto('geladeira', 2000, 5)
adicionar_produto('celular', 1000, 5)
remover_produto('celular')
listar_produtos()