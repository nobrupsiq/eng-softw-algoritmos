import math

raiz_quadrada = math.sqrt(121)
potencia = math.pow(8, 4)
arredondamento_cima = math.ceil(7.9) 
arredondamento_cima = math.floor(7.9)
valor_absoluto = math.fabs(-45.67)
fatorial = math.factorial(6)
logaritmo_natural = math.log2(20)
logaritmo_base_10 = math.log10(1000)
area_do_circulo = math.pi * math.pow(5, 2)
seno = math.sin(60)
coseno = math.cos(60)
tangente = math.tan(60)
hipotenusa = math.hypot(9, 12)

def circulo_info(raio):
    area = math.pi * math.pow(raio, 2)
    circuferencia = math.tau
    return area, circuferencia

arco_seno = math.asin(0.5)
arco_seno_convertido_para_graus = math.degrees(arco_seno)
trunque = math.trunc(7.987)
mdc = math.gcd(48, 18)
exponencial = math.exp(3)
graus_para_radianos = math.radians(90)
radianos_para_graus = math.degrees(math.radians(math.tau))
parte_fracionaria = math.modf(7.89)
logaritimo_base2 = math.log2(32)
logaritmo_base10 = math.log10(100)
arco_cosseno_em_graus = math.degrees(math.acos(0.5))
arco_tangente_em_graus = math.degrees(math.atan(1))
cosseno_hiperbolico = math.cosh(1)
seno_hiperbolico = math.sinh(1)
tangente_hiperbolica = math.tanh(1)
verificacao_numero_infinito = math.isinf(1e308)
verificar_nan = math.isnan(math.nan)
