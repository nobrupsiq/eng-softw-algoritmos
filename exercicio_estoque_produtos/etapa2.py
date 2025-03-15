# Etapa 2 - Reescreva o código com uma função menu essa função deve: Exibir as opções e executar as funções conforme a escolha do usuário

estoque = []

def menu(): 
    while True:
        print("""
    -------------- Gerenciamento de estoque --------------  
        Escolha uma opção:
            
        1 - Adicionar produto
        2 - Listar produtos
        3 - Atualizar quantidade de um produto
        4 - Remove produto
        5 - Sair   
    """)
        opcao = input('Digite sua opção: ')
        
        if opcao == '1':
            adicionar_produto()
        elif opcao == '2':
            listar_produtos()
        elif opcao == '3':
            atualizar_quantidade()
        elif opcao == '4':
            remover_produto()
        elif opcao == '5':
            print('Saindo do programa!')
            break
        else:
            print('Opção inválida.')

def adicionar_produto():
    nome = input('Nome do produto: ').capitalize()
    preco = float(input('Preço: '))
    quantidade = int(input('Quantidade: '))

    produto = {
        'nome': nome,
        'preco': preco,
        'quantidade': quantidade
    }
    estoque.append(produto)
    print('Produto adicionado com sucesso!')

def listar_produtos():
  if len(estoque) > 0:
    for i, produto in enumerate(estoque):
      resposta = f'{i+1}. Nome: {produto['nome'].capitalize()} | Preço: R$ {produto['preco']:.1f} | Quantidade: {produto['quantidade']}'
      print(resposta)
  else:
      print('Estoque vazio!')

def atualizar_quantidade():
    nome = input('Nome do produto para atualizar: ')
    quantidade = int(input('Nova quantidade: '))
    for produto in estoque:
        if produto['nome'] == nome.capitalize():
            produto['quantidade'] = quantidade
    print(f'Quantidade atualizada com sucesso!')

def remover_produto():
   nome = input('Nome do produto para remover: ').capitalize()
   for produto in estoque:
      if produto['nome'] == nome.capitalize():
         estoque.remove(produto)
   print('Produto removido com sucesso!')

menu()