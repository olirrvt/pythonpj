nome = str(input("Digite seu nome completo: ")).strip().title()
nomesep = nome.split()
print (f"Seu primeiro nome é {nomesep[0]}")
print (f"Seu último nome é {nomesep[len(nomesep)-1]}")

