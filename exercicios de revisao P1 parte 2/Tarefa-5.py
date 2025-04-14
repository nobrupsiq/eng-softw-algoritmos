# Uma loja oferece descontos progressivos conforme o valor da compra:
# • Até R$ 100 → 5%
# • De R$ 100,01 a R$ 500 → 10%
# • Acima de R$ 500 → 15%
# O sistema deve receber o valor da compra e calcular o valor final com desconto aplicado

def calcular_desconto(valor):
  if valor > 0 and valor <= 100:
    desconto = valor * 0.05
  elif valor <= 500:
    desconto = valor * 0.10
  else:
    desconto = valor * 0.15

  return valor - desconto

valor_do_produto = float(input('Valor do produto: '))
resultado = calcular_desconto(valor_do_produto)

print(f'Valor do produto com o desconto aplicado R${resultado}')