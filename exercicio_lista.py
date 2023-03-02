import os 
lista = []
cmd = 'cls'

while True:
    op= (input("informe uma opção: \n [I]ncerir [A]pagar [L]istar [S]air "))
    opcao = op.lower()
    if opcao == "i":
        os.system('')
        inserir = input("insira um item: ")
        lista.append(inserir)
    elif opcao == "a":
        os.system(cmd)
        indice_str = print(input("informe o indice que deseja apagar: "))
        try:
            indice = int(indice_str)
            del lista[indice]

        except ValueError:
            print("informe um indice inteiro")
        except IndexError:
            print("informe um index existente")

    
    elif opcao == "l":
        for i, items in enumerate(lista):
            print(i, items)
    
    elif opcao == "i":
        break
        


        


