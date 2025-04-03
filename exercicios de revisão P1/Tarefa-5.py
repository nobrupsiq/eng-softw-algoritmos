# Uma empresa precisa calcular os impostos sobre o salário dos funcionários, considerando três
# tributos:
# 1. INSS
#    7,5% para salários até R$ 1.500
#    9% para salários entre R$ 1.500,01 e R$ 3.000
#    12% para salários acima de R$ 3.000
# 2. IRPF (Imposto de Renda Pessoa Física)
#    Isento para salários até R$ 2.000
#    7,5% para salários entre R$ 2.000,01 e R$ 4.000
#    15% para salários acima de R$ 4.000
# O programa deve calcular o salário líquido após o desconto dos impostos.


def calculo_inss(salario):
    if salario > 0 and salario <= 1500:
        return salario * 0.075
    elif salario > 1500.01 and salario <= 3000:
        return salario * 0.12


def calculo_irpf(salario):
    if salario > 0 and salario <= 2000:
        return salario
    elif salario > 2000.01 and salario <= 4000:
        return salario * 0.075
    else:
        return salario * 0.15

def calcular_impostos(salario):
    imposto_inss = calculo_inss(salario)
    imposto_irpf = calculo_irpf(salario)
    calculo_total = salario - imposto_inss - imposto_irpf
    return f'Salário liquído -> R${calculo_total:.2f}'

resultado = calcular_impostos(3000)
print(resultado)