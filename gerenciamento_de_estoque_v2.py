# V2
# Problema: Gerenciamento de Estoque de uma Loja
# Versão 1: Uma loja deseja gerenciar seu estoque de produtos de forma eficiente. Para isso,
# precisa de um sistema que utilize DICIONARIOS e LISTAS para armazenar informações sobre os
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

estoque_de_produtos = {}

def adicionar_produto(cod, nome, quantidade, preco):
    if cod in estoque_de_produtos:
        print(f'Produto com o código: "{cod}" já existe!')
        return estoque_de_produtos
    estoque_de_produtos[cod] = [nome, quantidade, preco]
    print(f'Produto "{nome}" adicionado com sucesso!')
    return estoque_de_produtos


def atualizar_quantidade_de_estoque(cod, quantidade):
    if cod not in estoque_de_produtos:
        print(f'Produto com o código "{cod}" não encontrado no estoque!')
        return estoque_de_produtos
    estoque_de_produtos[cod][1] = quantidade
    print(f'Quantidade de "{estoque_de_produtos[cod][0]}" atualizada para "{quantidade}"!')
    return estoque_de_produtos

def listar_produtos():
    if not estoque_de_produtos:
        print('Nenhum produto cadastrado!')
        return estoque_de_produtos
    print('Estoque atual: ')
    for i, j in estoque_de_produtos.items():
        print(f'Codigo: {i} | Produto: {j[0]} | Quantidade: {j[1]} | Preço: R$ {j[2]:.2f}')
    return estoque_de_produtos

def calcular_valor_total_do_estoque():
    total = 0
    for i, j in estoque_de_produtos.items():
        total += j[1] * j[2]
    print(f'O valor total do estoque é de R$ {total:.2f}')
    return total


adicionar_produto(1, 'Camiseta', 10, 29.90)
adicionar_produto(2, 'Calça', 5, 59.90)
atualizar_quantidade_de_estoque(1, 20)

print(estoque_de_produtos)
listar_produtos()