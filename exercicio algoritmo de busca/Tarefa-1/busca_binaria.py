alvo = int(input('Qual o número deseja encontrar? '))

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

lista = [23, 5, 87, 12, 49, 3, 66, 71, 19, 34, 8, 56, 91, 14, 42]

resultado = busca_binaria(lista, alvo)

if resultado != -1:
    print(f'A posição do alvo {alvo} na lista: {resultado}')
else:
    print(f'Alvo não encontrado na lista!')