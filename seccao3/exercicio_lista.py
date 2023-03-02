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
        indice = int(input("informe o indice que deseja apagar: "))
        try:
            del lista[indice]

        except ValueError:
            print("informe um indice inteiro")
        except IndexError:
            print("informe um index existente")
        except Exception as error:
            print(error.message)
    
    elif opcao == "l":
        os.system(cmd)
        if len(lista) == 0:
            print("lista vazia")
        else:
            for i, items in enumerate(lista):
                print(i, items)
    
    elif opcao == "i":
        os.system(cmd)
        break
        


        


