# Escreva um programa em Python que contenha uma função chamada
# calcula_bonificacao.
# (A). Essa função deve receber dois parâmetros:
# i. taxa_bonus: A porcentagem de bonificação de produção
# concedida ao funcionário.
# ii. salario_base: O salário do funcionário antes da bonificação.
# A função deve calcular e retornar o novo salário do funcionário, já
# incluindo a bonificação. No programa principal, solicite ao usuário que
# informe o salário base e a taxa de bonificação, chame a função e exiba o
# salário base, salário final atualizado, bem como a bonificação concedida

def calcula_bonificação(taxa_bonus, salario_base):
    calculo = salario_base * (taxa_bonus / 100)
    return salario_base + calculo

salario = float(input('Informe o salário base: '))
bonificacao = int(input('Informe a bonificação: '))

resultado = calcula_bonificação(bonificacao, salario)

print(f"""
Salário base: R$ {salario:.2f}
Bonificação aplicada: {bonificacao}%
Salário final: R$ {resultado:.2f}
""")
