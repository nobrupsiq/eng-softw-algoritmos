# Problema: Gerenciamento de Estoque de uma Loja
# Versão 1: Uma loja deseja gerenciar seu estoque de produtos de forma eficiente. Para isso,
# precisa de um sistema que utilize dicionários e tuplas para armazenar informações sobre os
# produtos.

# Cada produto tem:
#   • Código (único)
#   • Nome
#   • Quantidade disponível
#   • Preço unitário

# O sistema deve permitir:
#   1. Adicionar novos produtos ao estoque.
#   2. Atualizar a quantidade de um produto existente.
#   3. Listar todos os produtos disponíveis.
#   4. Calcular o valor total do estoque.

# Testando como tuplas funcionam dentro de um dicionario
# teste = {
#     1: ('Monitor', 20, 50),
#     2: ('Geladeira', 4, 1200.23)
# }

# for i, j in teste.items():
#     print(i, j[2])

# Agora eu ja sei como eu acesso cada chave e cada valor
estoque_de_produtos = {}

def adicionar_produto(cod, nome, quantidade, preco):
    if cod in estoque_de_produtos:
        print(f'Produto com o código: "{cod}" já existe!')
        # Retornei a lista pq se eu não retornar a lista irá sobrescrever o meu produto
        return estoque_de_produtos
    estoque_de_produtos[cod] = (nome, quantidade, preco)
    print(f'Produto "{nome}" adicionado com sucesso!')
    return estoque_de_produtos

# Tomei uma surra aqui, tinha esquecido que tuplas são imutaveis, a maneira que consegui foi transformando a tupla em lista e depois transformar a lista em tupla de novo, não sei se é bom fazer isso, mas foi o que eu pensei.
def atualizar_quantidade_de_estoque(cod, quantidade):
    if cod not in estoque_de_produtos:
        print(f'Produto com o código "{cod}" não encontrado no estoque!')
        return estoque_de_produtos
    estoque_lista = list(estoque_de_produtos[cod])
    estoque_lista[1] = quantidade
    estoque_de_produtos[cod] = tuple(estoque_lista)
    print(f'Quantidade de "{estoque_de_produtos[cod][0]}" atualizada para "{quantidade}"!')
    return estoque_de_produtos

def listar_produtos():
    if not estoque_de_produtos:
        print('Nenhum produto cadastrado!')
        return estoque_de_produtos
    for i, j in estoque_de_produtos.items():
        print(f'Codigo: {i} | Produto: {j[0]} | Quantidade: {j[1]} | Preço: R$ {j[2]:.2f}')
    return estoque_de_produtos

# Depois que eu descobri esse looping na função acima, tudo ficou mais claro, então essa função ficou menos dificil de fazer.
def calcular_valor_total_do_estoque():
    total = 0
    for i, j in estoque_de_produtos.items():
        total += j[1] * j[2]
    print(f'O valor total do estoque é de R$ {total:.2f}')
    return total
