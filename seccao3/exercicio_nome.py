nome = input("informe seu nome:")
idade = input("Infoeme sua idade:")

if nome and idade:
    print(f'seu nome é {nome}')
    print(f'seu nome invertido é {nome[::-1]}')
    if ' ' in nome:
        print(f'seu nome contem espaço')
    else:
       print(f'seu nome não contem espaço')
    print(f"seu nome tem {len(nome)} letras")
    print(f"A peimeira letra do seu nome é: {nome[0]}")
    print(f"A ultima letra do seu nome é: {nome[-1]}")
else:
    print("Desculpe,deixou campos vazios")