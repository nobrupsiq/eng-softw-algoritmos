# 5. A empresa PVDM (Programadores Vão Dominar o Mundo) deseja conceder aumento salarial aos seus programadores. 
# O aumento será calculado conforme o salário atual do programador, de acordo com as seguintes regras:
#   (A). Salários até R$ 3000,00: aumento de 25%.
#   (B). Salários entre R$ 3000,01 e R$ 8000,00: aumento de 20%.
#   (C). Salários entre R$ 8000,01 e R$ 20000,00: aumento de 15%.
#   (D). Salários acima de R$ 20000,00: aumento de 4,5%.
# Escreva um programa que recebe o salário de um programador e calcula
# o salário atualizado com o aumento.

def calcular_aumento_salarial(salario):
    if salario > 0 and salario <= 3000:
        aumento = salario + (salario * 0.25)
    elif salario <= 8000:
        aumento = salario + (salario * 0.20)
    elif salario <= 20000:
        aumento = salario + (salario * 0.15)
    else:
        aumento = salario + (salario * 0.045)
    return aumento

salario_dev = float(input('Salário do programador: R$ '))

resultado = calcular_aumento_salarial(salario_dev)
print(f'Salário do programador atualizado para: R$ {resultado:.2f}')