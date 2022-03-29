import random
import time

print ("-" * 30)
print ("Eu escolhi um número de 0 a 5. ")
print ("-" * 30)
num = int(input("Digite qual número você acha que eu escolhi: "))
listanum = [0, 1, 2, 3, 4, 5]
sorteio = random.choice(listanum)
print ("Analisando sua resposta...")
time.sleep(4)
if num == sorteio:
    print ("ACERTOU!")
elif num > 5:
    print ("ERRO! Só pode ser entre 0 e 5...")

else:
    print ("Não foi dessa vez!")

print ("-" * 30)
print (f"O número escolhido foi {sorteio}!")
print ("-" * 30)