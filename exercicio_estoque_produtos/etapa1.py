# Etapa 1 - Utilize chamadas as funções

estoque_lista_dicionario = []

def adicionar_produto(nome, preco, quantidade):
    produto = {
        'nome': nome,
        'preco': preco,
        'quantidade': quantidade
    }
    estoque_lista_dicionario.append(produto)
    print('Produto adicionado com sucesso!')

def listar_produtos():
  for i, produto in enumerate(estoque_lista_dicionario):
    resposta = f'{i+1}. Nome: {produto['nome'].capitalize()} | Preço: R$ {produto['preco']:.1f} | Quantidade: {produto['quantidade']}'
    print(resposta)

def atualizar_quantidade(nome, quantidade):
    for produto in estoque_lista_dicionario:
        if produto['nome'] == nome.capitalize():
            produto['quantidade'] = quantidade
    print(f'Quantidade atualizada com sucesso!')

def remover_produto(nome):    
   for produto in estoque_lista_dicionario:
      if produto['nome'] == nome:
         estoque_lista_dicionario.remove(produto)
   print('Produto removido com sucesso!')

adicionar_produto('televisão', 2400, 20)
adicionar_produto('celular', 1500, 10)
remover_produto('Celular')
listar_produtos()

