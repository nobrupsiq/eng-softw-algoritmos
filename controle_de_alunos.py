# Problema: Sistema de Controle de Alunos
# Uma escola precisa de um sistema para gerenciar alunos e suas notas. O sistema deve
# armazenar as informações dos alunos e permitir:

# 1. Adicionar um novo aluno com seu nome e uma lista de notas.
# 2. Adicionar uma nota a um aluno existente.
# 3. Calcular a média das notas de um aluno.
# 4. Exibir todos os alunos e suas médias


alunos = {}

def adicionar_aluno(nome):
    if type(nome) == str: 
        alunos[nome] = []
        return f'Aluno "{nome}" adicionado!'
    else:
        return 'Erro... Digite um nome e não um número!'

def adicionar_nota(aluno, nota):
    try:
        if aluno in alunos:
            alunos[aluno] += [nota]
            return 'Nota adicionada!'
        else:
            return 'Aluno não encontrado!'
    except Exception as e:
        return f'Erro ao adicionar nota: {e}'

def calcular_media(aluno):
    if aluno not in alunos:
        return f'O aluno "{aluno}" não está na lista de alunos!'

    if not alunos[aluno]:
        return f'O aluno "{aluno}" não possui notas!'

    return f'A média do aluno {aluno}: {sum(alunos[aluno]) / len(alunos[aluno]):.2f}'

def listar_alunos_e_media():
    if not alunos:
        print('Lista de alunos vazia!')

    # Esse looping eu precisei ir buscar na documentação no W3School, muito bom!
    for nome, notas in alunos.items():
        if notas:
            media = sum(notas) / len(notas)
            print(f'Aluno: {nome} | Media das notas: {media:.2f}')
        else:
            print(f'Aluno: {nome} | Nenuma nota cadastrada!')

