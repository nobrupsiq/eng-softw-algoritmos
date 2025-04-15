# Crie um sistema de agenda em Python que permita:
#   1. Cadastrar contatos com nome, telefone e e-mail.
#   2. Listar todos os contatos cadastrados.
#   3. Buscar um contato pelo nome.
#   4. Excluir um contato.
# Os dados devem ser armazenados em uma lista de dicionários.
import time
agenda = []

# teste = [
#   {
#     'Nome': {'telefone': 9999999, 'email': 'teste@teste.com'}
#   },
#   {
#     'Nome': {'telefone': 9999999, 'email': 'teste@teste.com'}
#   },
#   {
#     'Nome': {'telefone': 9999999, 'email': 'teste@teste.com'}
#   }
# ]

def cadastrar_contato(nome, telefone, email):
  contato = {
    'Nome': nome, 
    'Telefone': telefone, 
    'Email': email
    }
  agenda.append(contato)

def listar_contatos():
  for i, contato in enumerate(agenda):
    print(f'{i+1}. Nome: {contato['Nome']} | Telefone: {contato['Telefone']} | Email: {contato['Email']}')

def buscar_contato(nome):
  for contato in agenda:
    if contato['Nome'] == nome:
      print(f'Nome: {contato['Nome']} | Telefone: {contato['Telefone']} | Email: {contato['Email']}')
      return

def excluir_contato(nome):
  for contato in agenda:
    if contato['Nome'] == nome:
      agenda.remove(contato)


while True:
  print("""
    ---- Sistema de Agenda ----\n
         1. Adicionar contato
         2. Listar todos os contados
         3. Buscar contato
         4. Excluir contato
         5. Sair
  """)
  opcao = input('Opcao: ')

  if opcao == '1':
    nome = input('Nome: ').capitalize()
    for contato in agenda:
      if contato['Nome'] == nome:
        print(f'O contato "{nome}" já existe na agenda!')
        break
    else:
      telefone = input('Telefone EX: (22)99999-9999: ')
      email = input('Email: ')
      cadastrar_contato(nome, telefone, email)
      print('\nAdicionando contado na agenda... ⌛')
      time.sleep(2)
      print(f'Contato "{nome}" adicionado com sucesso!')
  elif opcao == '2':
    if len(agenda) > 0:
      print('\nCarregando contatos... aguarde ⌛\n')
      time.sleep(2)
      listar_contatos()
    else:
      print('\nCarregando contatos... aguarde ⌛\n')
      time.sleep(2)
      print("Agenda vazia!")
  elif opcao == '3':
    nome = input('Nome: ').capitalize()
    for contato in agenda:
      if contato['Nome'] == nome:
        print('\nBuscando contato... aguarde ⌛')
        time.sleep(2)
        print(f'Contato "{nome}" encontrado!\n')
        buscar_contato(nome)
        break
    else:        
      print('\nBuscando contato... aguarde ⌛')
      time.sleep(2)
      print(f'O contado "{nome}" não está na agenda.')
  elif opcao == '4':
    nome = input('Nome: ').capitalize()
    for contato in agenda:
      if contato['Nome'] == nome:
        print('Buscando contato... aguarde ⌛')
        time.sleep(2)
        excluir_contato(nome)
        print(f'Contato "{nome}" excluido com sucesso!\n')
        break
    else:
      print('\nBuscando contato... aguarde ⌛')
      time.sleep(2)
      print(f'O contato "{nome}" não existe na agenda!')
  elif opcao == '5':
    print('Saindo...')
    break