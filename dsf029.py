velocidade = int(input("Digite a velocidade atual de um carro: "))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print (f"VOCÊ ATINGIU O LIMITE DE VELOCIDADE! que é de 80km/h...IRÁ RECEBER UMA MULTA DE R$ {multa},00 REAIS")
else: 
    print ("Tenha um bom dia! Dirija com segurança!")

