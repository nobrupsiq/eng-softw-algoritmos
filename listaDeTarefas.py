listaDeTarefas = []

def adicionarTarefa(tarefa):
    listaDeTarefas.append(tarefa)
    print(f'Tarefa: "{tarefa}" Adicionado(a) com sucesso!')
    return listaDeTarefas

def removerTarefa(tarefa):
    if tarefa in listaDeTarefas:
        listaDeTarefas.remove(tarefa)
        print(f'A tarefa {tarefa} foi removida com sucesso!')
        return listaDeTarefas
    else:
        return f'"{tarefa}" não se encontra em sua lista!'

def exibirTarefas():
    return print(listaDeTarefas)

