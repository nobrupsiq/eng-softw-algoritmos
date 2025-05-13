# Escreva uma função recursiva que verifique se uma string é um palíndromo. Um
# palíndromo é uma palavra ou frase que se lê da mesma forma de trás para frente,
# ignorando espaços, maiúsculas e minúsculas. Por exemplo, "arara" é um palíndromo.

def palindromo(nome):
  format_nome = nome.replace(' ', '').lower()
  if len(format_nome) == 0 or len(format_nome) == 1:
    return True
  
  if format_nome[0] != format_nome[-1]:
    return 'Não é um palindromo!'
  else:
    return palindromo(format_nome[1: -1])

resultado = palindromo('arara')
print(resultado)