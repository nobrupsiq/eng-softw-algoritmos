# Exceções personalizadas: Escreva uma função que verifica se uma senha
# possui no mínimo 8 caracteres e pelo menos um número. Se a senha não
# atender aos requisitos, levante uma exceção com uma mensagem
# personalizada. Trate a exceção e mostre a mensagem ao usuário.


# O CÓDIGO E A SOLUÇÃO QUE CONSEGUI PENSAR E FAZER
def verificador_de_senha():
  try:
    senha = input('Senha: [Min 8 caracters + 1 numero]: ')
    split_senha = list(senha)
    numbers = '0, 1, 2, 3, 4, 5, 6, 7, 8, 9'
    flag = False

    if len(senha) < 8:
      print('Senha deve possuir no mínimo 8 caracteres!')
    else:
      for i in split_senha:
        for j in numbers:
          if i == j:
            flag = True
    if flag == True:
      print('Senha aceita!')
    else:
      print('A senha deve possuir pelo menos um número!')
  except Exception as e:
    print('Erro: ', e)
  else: 
    print('Programa executado.')
  finally:
    print('Programa encerrado.')

# Novo aprendizado, não sabia que dava pra usar o Exception assim personalizado
class SenhaInvalidaError(Exception):
    pass

def verificador_de_senha2():
    try:
      senha = input('Senha: [Min 8 caracteres + 1 número]: ')
      
      # Verificar se o tamanho da senha é menor que 8 caracteres
      if len(senha) < 8:
        raise SenhaInvalidaError('A senha deve ter no mínimo 8 caracteres.')
      
      # Verifica se tem algum digito numerico na senha
      if not any(char.isdigit() for char in senha):
        raise SenhaInvalidaError('A senha deve conter pelo menos um número.')
      
      print('Senha aceita!')
    except SenhaInvalidaError as e:
      print('Erro:', e)
    else:
      print('Programa executado.')
    finally:
      print('Programa encerrado.')

verificador_de_senha2()