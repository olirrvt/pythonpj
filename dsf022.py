
nome = str(input("Qual é o seu nome? ")).strip()
print (f"O seu nome em maiúsculas é {nome.upper()}")
print (f"O seu nome em minúsculas é {nome.lower()}")
print (f"Seu nome ao todo tem {len(nome) - nome.count(' ')} letras")
print (f"Seu primeiro nome tem {nome.find(' ')} letras")