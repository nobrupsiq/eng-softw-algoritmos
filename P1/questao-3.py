# Crie um programa em Python que implemente uma função chamada
# calcula_imposto_de_renda. A função deve receber um único parâmetro:
# salário: o valor do salário bruto de um indivíduo.
# Com base na tabela de alíquotas abaixo, a função deve calcular e
# retornar o valor do imposto de renda devido:

def calcula_imposto_de_renda(salario):
    if salario > 0 and salario <= 2112:
        imposto = 0
    elif salario <= 2826.66:
        imposto = salario * 0.075 + 158.4
    elif salario <= 3751.06:
        imposto = salario * 0.15 + 370.4
    elif salario <= 4664.69:
        imposto = salario * 0.225 + 651.73
    else:
        imposto = salario * 0.275 + 884.96
    
    return imposto

salario_bruto = float(input('Salário bruto: '))

resultado = calcula_imposto_de_renda(salario_bruto)
print(f"""
Salário bruto: R$ {salario_bruto:.2f}
Imposto de Renda Devido: R$ {resultado:.2f}
""")