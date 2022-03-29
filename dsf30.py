import time
print ("Nesse programa iremos identificar se o número é PAR ou ÍMPAR!")
num = int(input("Digite o número desejado: "))
print ("Analisando...")
time.sleep(2)
verificador = num % 2
if verificador == 0:
    print (f"O número {num} é PAR!")
else:
    print (f"O número {num} é ÍMPAR!")