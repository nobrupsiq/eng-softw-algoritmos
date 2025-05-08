# Escreva uma função recursiva que calcule o máximo divisor comum (MDC) de dois
# números inteiros a e b.

# CASO BASE
#  x = 2 | y = 0 RETURN 2
#  x = 0 | y = 50 RETURN 50

# FORMULA
# x / y = é tanto e sobra tanto
# y / pelo resto de x / y = é tanto
# Pegar o ultimo numero que seja diferente de zero

# EXEMPLO:
#   X = 40 Y = 30
#   40 / 30 = 10 E SOBRA 10 <- ULTIMO NUMERO DIFERENTE DE ZERO
#   30 / 10 = 10 E SOBRA ZERO

def calcular_mdc(x, y):
  if x == 0:
    return y
  elif y == 0:
    return x
  
  return calcular_mdc((x % y), y % (x % y))

resultado = calcular_mdc(89, 65)
print(resultado)




