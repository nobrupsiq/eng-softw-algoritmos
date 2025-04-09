# Um clube esportivo quer classificar seus atletas de acordo com a idade. Implemente um
# programa que receba o nome e a idade do atleta e classifique nas seguintes categorias:
#   • "Infantil" → até 12 anos
#   • "Juvenil" → 13 a 17 anos
#   • "Adulto" → 18 a 35 anos
#   • "Master" → acima de 35 anos
# O sistema deve permitir o cadastro de vários atletas e exibir a lista com seus nomes, idades e
# categorias.


lista_de_atletas = []

def adicionar_atleta(nome, idade):
    if idade > 0 and idade <= 12:
        atleta = {
            "Nome": nome,
            "Idade": idade,
            "Categoria": "Infantil"
        }
        lista_de_atletas.append(atleta)

    elif idade > 12 and idade <= 17:
        atleta = {
            "Nome": nome,
            "Idade": idade,
            "Categoria": "Juvenil"
        }
        lista_de_atletas.append(atleta)

    elif idade > 18 and idade <= 35:
        atleta = {
            "Nome": nome,
            "Idade": idade,
            "Categoria": "Adulto"
        }
        lista_de_atletas.append(atleta)

    else:
        atleta = {
            "Nome": nome,
            "Idade": idade,
            "Categoria": "Master"
        }
        lista_de_atletas.append(atleta)


def exibir_atletas():
    if len(lista_de_atletas) > 0:
        for i in lista_de_atletas:
            return f'Nome: {i['Nome']} | Idade: {i['Idade']} | Categoria: {i['Categoria']}'
    else:
        print('Lista de atletas vazia!')
while True:
    print("""
    ----- Sistema de atletas -----

        1. Adicionar atleta
        2. Exibir atletas
        3. Sair
""")
    opcao = input('Opcão: ')

    if opcao == '1':
        nome = input('Nome do atleta: ').capitalize()
        idade = int(input('Idade do atleta: '))
        adicionar_atleta(nome, idade)
    elif opcao == '2':
        exibir_atletas()
    elif opcao == '3':
        print('Saindo...')
        break
    else:
        print('Você digitou algo errado!')
        