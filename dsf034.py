salario = float(input("Qual é o valor do seu salário? R$ "))

if salario > 1250:
     aumento = (10/100) * salario
     total = aumento + salario
     print (f"O seu salário recebeu um aumento de 10% e passou a ser R$ {(total):.2f}")

else:
    aumento = (15/100) * salario
    total = aumento + salario
    print (f"O seu salário recebeu um aumento de 15% e passou a ser R$ {(total):.2f}")

print ("Muito obrigado e volte sempre!")
