# Escreva uma função recursiva que encontre todos os anagramas de uma string.

def gerar_anagramas(s):
    if len(s) <= 1:
        return [s]
    
    anagramas = [] 
    
    for i in range(len(s)):
        letra_fixa = s[i]        
        restante = s[:i] + s[i+1:]          
      
        for anagrama in gerar_anagramas(restante):
            novo_anagrama = letra_fixa + anagrama
            anagramas.append(novo_anagrama)
    
    return anagramas

resultado = gerar_anagramas('teste')
print(resultado)