print ("*" * 30)
print ("   ANALISADOR DE TRIÃNGULOS")
print ("*" * 30)
segmento1 = float(input("Digite o primeiro segmento: "))
segmento2 = float(input("Digite o segundo segmento: "))
segmento3 = float(input("Digite o terceiro segmento: "))

analisador = segmento1 + segmento2
analisador2 = segmento3 + segmento2
analisador3 = segmento1 + segmento3

if segmento1 + segmento2 > segmento3 and segmento2 + segmento3 > segmento1 and segmento1 + segmento3 > segmento2:
    print ("Os seguintes dados FORMAM um triângulo!")
else:
    print ("Os seguintes dados NÃO formam um triângulo!")
print ("*" * 30)
