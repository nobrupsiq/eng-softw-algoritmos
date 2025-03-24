alvo = int(input('Qual o número deseja encontrar? '))
tamanho_da_lista = int(input('Quer procurar em uma lista de quantos numeros? '))

lista_de_numeros = []

for numero in range(1, tamanho_da_lista):
    lista_de_numeros.append(numero)

def busca_binaria(lista, alvo):
    lista_ordenada = sorted(lista)
    pos_inicial = 0
    pos_final = len(lista_ordenada) -1

    while pos_inicial <= pos_final:
        pos_meio = (pos_inicial + pos_final) // 2

        if lista_ordenada[pos_meio] == alvo:
            return pos_meio
        if lista_ordenada[pos_meio] > alvo:
            pos_final = pos_meio - 1
        else:
            pos_inicial = pos_meio + 1
    return -1


resultado = busca_binaria(lista_de_numeros, alvo)

if resultado != -1:
    print(f'A posição do alvo {alvo} na lista é: {resultado}')
else:
    print(f'Alvo não encontrado na lista!')