teste = "sergio" 
# print(teste[2])
print("i" in teste)
print("-" * 10)
print("j" in teste)

print("-" * 10)

nome = input("informe seu nome:")
encontrar =input("infome o que quer encontar")

if encontrar in nome:
    print(f"{encontrar} se encontra em {nome}")
else:
    print(f"{encontrar} nao se encontra em {nome}")
