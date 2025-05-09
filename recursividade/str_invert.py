# Escreva uma função recursiva que inverta uma string. Por exemplo, se a entrada for "python", a função deve retornar "nohtyp".

def invertString(nome):
  if len(nome) == 0:
    return nome

  return nome[-1] + invertString(nome[0:-1])

resultado =  invertString('python')

print(resultado)

