# Simulação de transações: Crie um programa que simule uma transferência
# bancária. Peça ao usuário o saldo da conta e o valor da transferência. Caso o
# saldo seja insuficiente, levante uma exceção do tipo ValueError com a
# mensagem "Saldo insuficiente". Trate a exceção adequadamente e informe o
# usuário.

def transferencia_bancaria():
  try:
    saldo = float(input('Saldo da conta R$ '))
    transferencia = float(input('Valor da trasnferencia R$ '))

    if saldo < transferencia:
      raise ValueError('Saldo insuficiente.')
    
  except ValueError as err:
    print('Erro:', err)
  else:
    print('Transferencia realizada!')
  finally:
    print('Encerrando o programa!')

transferencia_bancaria()