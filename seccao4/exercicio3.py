
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

respostas_corretas = 0
respostas_incorretas = 0
for pergunta in perguntas:
    print("Pergunta:",pergunta['Pergunta'] )
    print()
    op = pergunta['Opções']
    for i, op in enumerate(op):
        print(f"({i})",op)
        print()
        
    opcao = (input("Informe um opção:"))

    escolha_int = None 
    acertou = False
    teste =pergunta['Opções']
    qnt_op = len(teste)
    resposta = pergunta["Resposta"]
    
    if opcao.isdigit():
        escolha_int = int(opcao)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qnt_op:
            if teste[escolha_int] == resposta:
                acertou= True

    if acertou:
        print("acertou!!!")
        respostas_corretas += 1
    else:
        print("errou")
        respostas_incorretas += 1 

print(f'Você acertou {respostas_corretas} e errou {respostas_incorretas} de {len(perguntas)}')
