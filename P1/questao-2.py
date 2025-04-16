# Você deve criar um programa em Python que utilize um dicionário para
# armazenar as informações de funcionários de uma empresa. O programa
# deve ser capaz de fazer o seguinte:
#   (A) Perguntar o nome, o salário e o cargo de cada colaborador.
#   (B) Armazenar essas informações em um dicionário, onde a chave
# será o nome do colaborador e o valor será outro dicionário com
# as informações de salário e cargo.
#   (C)O programa deve permitir ao usuário consultar o salário e o
# cargo de um colaborador através do seu nome.
#    (D)O programa também deve permitir que o usuário liste todos os
# funcionários cadastrados, mostrando todas as informações.

import time

funcionarios = {}

def adicionar_funcionario(nome, salario, cargo):
    funcionarios[nome] = {}
    funcionarios[nome]['Salario'] = salario
    funcionarios[nome]['Cargo'] = cargo
    return nome, salario, cargo

def consultar_funcionario(nome):
    for nome, dados in funcionarios.items():
        print(f'Funcionário: {nome} | Salário: {dados['Salario']:.2f} | Cargo: {dados['Cargo']}')
    return nome

def listar_funcionarios():
    for nome, dados in funcionarios.items():
        print(f'Funcionário: {nome} | Salário: {dados['Salario']:.2f} | Cargo: {dados['Cargo']}')
    return nome, dados


while True:
    print("""
        --- Sistema de funcionários ---
            
            1. Adicionar funcionário
            2. Consultar funcionário
            3. Listar todos os funcionários
            4. Sair
    """)
    opcao = input('Opcao: ')

    if opcao == '1':
        nome = input('Nome do funcionário: ').capitalize()
        if nome not in funcionarios:
            salario = float(input('Salário do funcionário R$ '))
            cargo = input('Cargo do funcionário: ').capitalize()
            adicionar_funcionario(nome, salario, cargo)
            print('\nCadastrando funcionário.... Aguarde ⏳')
            time.sleep(2)
            print('Funcionário cadastrado com sucesso!')
        else:
            print('\nCadastrando funcionário.... Aguarde ⏳')
            time.sleep(2)
            print(f'Funcionário "{nome}" já existe na lista de funcionários!')
    elif opcao == '2':
        nome = input('Nome do funcionário: ').capitalize()
        if nome not in funcionarios:
            print('\nBuscando funcionário... Aguarde ⏳')
            time.sleep(2)
            print(f'Funcionário "{nome}" não encontrado!')
        else:
            print('\nBuscando funcionário... Aguarde ⏳')
            time.sleep(2)
            print('\nFuncionário encontrado!')
            consultar_funcionario(nome)
    elif opcao == '3':
        if len(funcionarios) > 0:
            print('\nCarregando a lista de funcionários... aguarde ⏳\n')
            time.sleep(2)
            listar_funcionarios()
        else:
            print('\nCarregando lista de funcionários... aguarde ⏳\n')
            time.sleep(2)
            print("Lista de funcionários vazia!")
    elif opcao == '4':
        print('Saindo...')
        break
    else:
        print('Ops... Você digitou algo errado! Vamos outra vez.')

