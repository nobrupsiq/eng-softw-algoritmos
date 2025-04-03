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
        calculo = salario * 7.5
        return  calculo


# def impostos(salario):
#     #INSS
#     if salario > 0 and salario <= 1500:

#     #IRPF

resultado = calculo_inss(1500)
print(resultado)