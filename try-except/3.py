# Bloco else e finally: Escreva um programa que solicite um número ao
# usuário. Se o número for maior que 10, exiba uma mensagem dizendo que o
# número é válido. Utilize o bloco else para imprimir que o programa foi
# executado com sucesso, e o bloco finally para imprimir Programa
# encerrado


def verificar_numero():
  try:
    numero = int(input('Digite um número: '))
    if numero > 10:
      print('Número válido!')
  except Exception as e:
    print('Um erro ocorreu!', e)
  else:
    print('Programa executado com sucesso!')
  finally:
    return 'Programa encerrado!'


print(verificar_numero())