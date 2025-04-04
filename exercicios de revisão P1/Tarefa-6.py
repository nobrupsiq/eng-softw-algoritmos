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


materia = input('Qual a matéria: ')

def adicionar_aluno(nome, notas):
    lista_de_alunos[materia.capitalize()][nome] = {}
    lista_de_alunos[materia.capitalize()][nome] = notas
    return lista_de_alunos


adicionar_aluno('Bruno', [2,5])
adicionar_aluno('Borba', [4,1])

for disciplina, nome in lista_de_alunos.items():
    print(nome.get('Borba'))

# print(lista_de_alunos)
