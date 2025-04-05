# Sistema de Cadastro de Alunos
# Uma escola precisa de um sistema para cadastrar alunos e armazenar suas notas em diferentes
# disciplinas. O sistema deve permitir:
#   1. Adicionar um aluno com seu nome e notas.
#   2. Exibir todos os alunos cadastrados com suas respectivas notas.
#   3. Calcular a média de cada aluno e indicar se ele está aprovado (média ≥ 7) ou
# reprovado (média < 7).

lista_de_alunos ={}

def adicionar_aluno_e_notas(nome, notas, materia):
    if materia not in lista_de_alunos:
      lista_de_alunos[materia] = {}
    
    lista_de_alunos[materia][nome] = {}
    lista_de_alunos[materia][nome]["notas"] = notas
    return lista_de_alunos
 


def exibir_alunos_e_notas():
    for materia, alunos in lista_de_alunos.items():
        print(f'\nMatéria: {materia}')
        for nome, nota_do_aluno in alunos.items():
            notas = ', '.join(list(map(str, nota_do_aluno['notas']))) # Essa eu tive que pesquisar... As notas estavam sendo exibidas assim Notas: [3,4,5] Dentro de uma lista... Não estava conseguindo tirar os colchetes para exibição. Pesquisei, mas o importante é que eu entendi o que esta acontecendo nessa linha de código.
            print(f' -> Aluno(a): {nome} | Notas: {notas}')

def calcular_media_dos_alunos():
    for materia, alunos in lista_de_alunos.items():
        print(f'\nMatéria: {materia}')
        for nome, nota_dos_alunos in alunos.items():
            media = sum(nota_dos_alunos['notas']) / len(notas)
            if media >= 7:
              print(f' -> Nome: {nome} | Média: {media:.2f} | Aluno(a) aprovado!')
            else:
              print(f' -> Nome: {nome} | Média: {media:.2f} | Aluno(a) reprovado!')
  
while True:
    print("""
    ----- Cadastro de Aluno -----
          
     1 - Adicionar aluno e nota
     2 - Exibir alunos e notas
     3 - Calcular média dos alunos
     4 - Sair
    """)

    opcao = input('Sua escolha: ')

    if opcao == '1':
        materia = input('Qual a matéria? ').capitalize()
        nome = input('Nome do aluno: ').capitalize()
        notas = [float(notas.strip().replace(',', '.')) for notas in input('Digite as notas separadas por espaço: ').split(' ')] # Com essa linha de codigo eu vou garantir que se o usuario digitar 5,3 o meu algoritmo transforme essa virgula por um ponto. O strip vai juntar todas as notas, o replace vai substituir virgula por ponto.
        adicionar_aluno_e_notas(nome, notas, materia)
    elif opcao == '2':
        exibir_alunos_e_notas()
    elif opcao == '3':
        calcular_media_dos_alunos()
    elif opcao == '4':
        print('Saindo...')
        break
    else:
        print("Você digitou algo errado! Vamos de novo.")
    

print(lista_de_alunos)