# Uma empresa deseja um programa para calcular o valor de impostos sobre um produto,
# considerando dois tributos:
#   1. ICMS (Imposto sobre Circulação de Mercadorias e Serviços) → 18% sobre o valor
#   do produto.
#   2. ISS (Imposto sobre Serviços) → 5% sobre o valor do serviço.
# O usuário informará o tipo de bem (mercadoria ou serviço) e o valor, e o sistema calculará o
# imposto devido.

def calcular_icms(valor):
    return  valor * 0.18

def calcular_iss(valor):
    return  valor * 0.05

tipo_de_bem = input("Qual o tipo de bem? Digite -> [Produto] ou [Serviço]: ").lower()
valor = float(input("Qual o valor R$: "))

def calcular(tipo_de_bem, valor):
    if tipo_de_bem == 'produto':
        return f'Imposto ICMS devido R${calcular_icms(valor):.2f}'
    else:
        return f'Imposto ISS devido R${calcular_iss(valor):.2f}'

resultado = calcular(tipo_de_bem, valor)
print(resultado)
