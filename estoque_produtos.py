# Crie um programa em Python que gerencie o estoque de uma loja. O programa deve permitir:

  # 1. Cadastrar um novo produto, armazenando nome, preço e quantidade em estoque.
  # 2. Exibir a lista de produtos cadastrados com todas as informações.
  # 3. Atualizar a quantidade de um produto existente no estoque.
  # 4. Remover um produto do estoque pelo nome.

# O programa deve armazenar os produtos em uma lista de dicionários, onde cada dicionário
# representa um produto com as seguintes chaves:
#   • "nome" (string)
#   • "preco" (float)
#   • "quantidade" (int)

# 1 - Adicionar produto
# 2 - Listar produtos
# 3 - Atualizar quantidade
# 4 - Remover produto
# 5 - Sair 

estoque = []

def adicionar_produto(nome, preco, quantidade):
  produto = {
    'nome': nome,
    'preco': preco,
    'quantidade': quantidade
  }
  estoque.append(produto)
  print('Produto adicionado com sucesso!')

def exibir_produtos():
  for i, produto in enumerate(estoque):
    resposta = f'{i+1}. Nome: {produto['nome'].capitalize()} | Preço: R$ {produto['preco']:.1f} | Quantidade: {produto['quantidade']}'
    print(resposta)

adicionar_produto('computador', 2500, 20);
adicionar_produto('placa de video', 3000, 7);

exibir_produtos()
  