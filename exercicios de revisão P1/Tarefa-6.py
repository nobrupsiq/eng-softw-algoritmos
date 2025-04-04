# Sistema de Cadastro de Alunos
# Uma escola precisa de um sistema para cadastrar alunos e armazenar suas notas em diferentes
# disciplinas. O sistema deve permitir:
#   1. Adicionar um aluno com seu nome e notas.
#   2. Exibir todos os alunos cadastrados com suas respectivas notas.
#   3. Calcular a média de cada aluno e indicar se ele está aprovado (média ≥ 7) ou
# reprovado (média < 7).

lista_de_alunos ={
    "Matematica": {},
    "Portugues": {},
    "Historia": {}
}


def adicionar_aluno_e_notas(nome, notas):
    materia = input('Qual a matéria? ')
    lista_de_alunos[materia.capitalize()][nome] = {}
    lista_de_alunos[materia.capitalize()][nome]["notas"] = [notas]
    return lista_de_alunos


def exibir_alunos_e_notas():
    for materia, alunos in lista_de_alunos.items():
        print(f'Matéria: {materia}')
        for nome, nota_do_aluno in alunos.items():
            notas = ', '.join(list(map(str, nota_do_aluno['notas']))) # Essa eu tive que pesquisar... As notas estavam sendo exibidas assim Notas: [3,4,5] Dentro de uma lista... Não estava conseguindo tirar os colchetes para exibição. Pesquisei, mas o importante é que eu entendi o que esta acontecendo nessa linha de código.
            print(f'Aluno: {nome} | Notas: {notas}')


while True:

    print("""
    ----- Cadastro de Aluno -----
          
     1 - Adicionar aluno e nota
     2 - Exibir alunos e notas
     3 - Calcular média dos alunos
          
    """)

    opcao = input('Sua escolha: ')

    if opcao == '1':
        adicionar_aluno_e_notas()