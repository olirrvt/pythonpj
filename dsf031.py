
print ("=~" *15)
print ("    PASSAGEM DE ÔNIBUS")
print ("=~" *15)

distancia = float(input("Qual a distância da viagem? "))

if distancia <= 200:
    valorp = distancia * 0.50
    print (f"Você irá pagar R$ {(valorp):.2f} por {distancia} km/h.")
else:
    valorg = distancia * 0.45
    print (f"Você irá pagar R$ {(valorg):.2f} por {distancia} km/h.")

print ("=~" *15)
print ("Boa viagem!")