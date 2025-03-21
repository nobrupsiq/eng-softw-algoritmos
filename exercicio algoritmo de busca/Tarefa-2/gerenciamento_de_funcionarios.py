# A empresa Algtech empresa possui um banco de dados contendo 100.000 funcionários. Cada 
# funcionário possui um ID único e um nome.
# O setor de Recursos Humanos (RH) frequentemente precisa buscar funcionários pelo ID. 
# Existem dois cenários distintos:
#   1. Cenário 1: A lista de funcionários não está ordenada.
#   2. Cenário 2: A lista de funcionários está ordenada pelo ID.
# A empresa quer saber qual método de busca é mais eficiente para recuperar os dados do 
# funcionário e melhorar a performance do sistema.


import random
import string

funcionarios = []

def gerar_nome():
    letras = string.ascii_lowercase
    nome = ''.join(random.choices(letras, k=5))  # Nome de 5 letras
    sobrenome = ''.join(random.choices(letras, k=7))  # Sobrenome de 7 letras
    return nome.capitalize() + " " + sobrenome.capitalize()

for i in range(1, 5):
    funcionario = {
        "id": i,
        "nome": gerar_nome()
    }

    funcionarios.append(funcionario)

print(funcionarios)

[
    {'id': 1, 'nome': 'Mozij Bwxugth'}, 
    {'id': 2, 'nome': 'Lfuhx Ngvwrlu'}, 
    {'id': 3, 'nome': 'Zocad Owzyeml'}, 
    {'id': 4, 'nome': 'Oymgc Agcglfp'}
]


