import math
ângulo = float(input("Digite o valor de um ângulo: "))
seno = math.sin(math.radians(ângulo))
cos = math.cos(math.radians(ângulo))
tan = math.tan(math.radians(ângulo))
print (f'O ângulo de {ângulo} tem o SENO de {(seno):.2f}.')
print (f'O ângulo de {ângulo} tem o COSSENO de {(cos):.2f}.')
print (f'O ângulo de {ângulo} tem a TANGENTE de {(tan):.2f}.')
