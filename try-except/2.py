usuario_cor = input('Digite o nome de uma cor: ')

cores = {
    'vermelho': (255, 0, 0), 
    'verde': (0, 255, 0), 
    'azul': (0, 0, 255)
}

def selecao_de_cor(usuario_cor):
    try:
        print(f'{usuario_cor} = rgb{cores[usuario_cor]}')
        
    except KeyError:
        print(f'Erro! Cor não encontrada!')
    except Exception as e:
        print(f'Erro desconhecido: {e}')
    finally:
        return 'Fim!'
    
resultado = selecao_de_cor(usuario_cor)
print(resultado)
