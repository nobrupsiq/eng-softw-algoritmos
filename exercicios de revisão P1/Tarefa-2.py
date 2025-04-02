# Uma empresa de transporte deseja classificar seus motoristas com base na quantidade e
# gravidade das multas recebidas no último ano. As categorias são:
#   • "Motorista Excelente" → Nenhuma multa registrada.
#   • "Motorista Bom" → No máximo 2 multas leves.
#   • "Motorista Regular" → Até 4 multas leves ou 1 multa grave.
#   • "Motorista Ruim" → Mais de 4 multas leves ou até 2 multas graves.
#   • "Motorista Perigoso" → Mais de 2 multas graves ou qualquer multa gravíssima.
# O sistema deve receber a quantidade de multas leves, graves e gravíssimas e classificar o
# motorista.

multa_leve = int(input('Multas leves: '))
multa_grave = int(input('Multas graves: '))
multa_gravissima = int(input('Multas gravíssimas: '))

def classificar_motorista(multa_leve, multa_grave, multa_gravissima):
  if multa_gravissima > 0 or multa_grave > 2:
    return 'Motorista Perigoso!'
  if multa_leve > 0 and multa_leve <= 2:
    return 'Motorista Bom!'
  elif (multa_leve > 4 ) or (multa_grave == 2):
    return 'Motorista Ruim!'
  elif (multa_leve > 2 and multa_leve <= 4) or (multa_grave == 1):
    return 'Motorista Regular!'
  else:
    return 'Motorista Excelente!'
  

resultado = classificar_motorista(multa_leve, multa_grave, multa_gravissima)
print(resultado)

