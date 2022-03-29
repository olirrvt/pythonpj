import datetime
print ("~" * 50)
print ("Se quiser verificar o ano atual digite o número 0!")
print ("~" * 50)
ano = int(input("Qual é o ano que deseja verificar? "))
if ano == 0:
    ano = datetime.date.today().year
if ano % 4 == 0 and ano % 100 != 0:
    print (f"O ano de {ano} é um ano BISSEXTO!")
else:
    print (f"O ano de {ano} NÃO é um ano BISSEXTO")