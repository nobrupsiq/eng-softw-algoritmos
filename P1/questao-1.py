# Escreva um programa em Python que tenha uma função chamada
# calcular_media. Esta função deve receber uma lista de notas de um aluno e
# calcular a média dessas notas. O programa principal deve:
#   (A). Solicitar ao usuário que informe o nome do aluno.
#   (B). Solicitar ao usuário que informe as notas do aluno (o número de notas pode ser variável, mas o programa deve permitir que o usuário
# adicione pelo menos 7 notas).
#   (C). Chamar a função calcular_media passando a lista de notas e exibir
# a média das notas.
#   (D). Caso a média seja superior ou igual a 8, exibir que o aluno foi
# # aprovado. Caso contrário, exibir que o aluno foi reprovado.


def calcular_media(notas):
    return sum(notas) / len(notas)

nome = input('Nome do aluno: ').capitalize()

while True:
  notas = input("Digite as notas separadas por espaço (Minimo 7 notas): ")
  notas.replace(',', '.')
  notas_do_aluno = list(map(float, notas.split()))


  if len(notas_do_aluno) < 7:
    print("Digite pelo menos 7 notas!")
  else:
    break

media = calcular_media(notas_do_aluno)

if media >= 8:
  print(f'Aluno: {nome} | Média: {media:.2f} | Aluno aprovado!')
else: 
  print(f'Aluno: {nome} | Média: {media:.2f} | Aluno reprovado!')

