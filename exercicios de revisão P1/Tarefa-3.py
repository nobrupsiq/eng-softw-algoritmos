# Uma pessoa deseja um programa para gerenciar suas tarefas diárias. O sistema deve permitir:
#   • Adicionar uma nova tarefa à lista de tarefas pendentes.
#   • Listar todas as tarefas pendentes.
#   • Marcar uma tarefa como concluída, removendo-a da lista.

lista_de_tarefas_pendentes = []

def adicionar_tarefa(tarefa):
  lista_de_tarefas_pendentes.append(tarefa)
  return lista_de_tarefas_pendentes

def listar_tarefas_pendentes():
  if len(lista_de_tarefas_pendentes) > 0:
    return '\n'.join(lista_de_tarefas_pendentes) # Não utilizei um for porque estava retornando sempre none, porque a função só exibe as tarefas e não retorna nada, porém quando eu dou um return tarefa, exibe apenas a primeira tarefa da lista. Então adicionei uma quebra de linha dentro de uma string e utilizei o metodo join para agrupar cada item da lista. com o /n no inicio irá exibir uma tarefa embaixo de outro.
  else:
    return 'Lista de tarefas vazia!'
  
def concluir_tarefa(nome):
  for item in lista_de_tarefas_pendentes:
    if item == nome:
      lista_de_tarefas_pendentes.remove(item)

adicionar_tarefa('Jogar o lixo fora')
adicionar_tarefa('Estudar')

x = listar_tarefas_pendentes()
print(x)