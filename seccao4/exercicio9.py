import os 
lista =  []
refazer = []

def adicionar(tarefa, lista):
    lista.append(tarefa)
    return tarefa

def listar(lista):
    print("entrei na funcao ")
    if not lista:
        print("Nenhuma tarefa para listar")
        return
    print("Tarefas:")
    for i in lista:
        print(i)
        
def desfazer(lista,refazer):
    if not lista:
        print("Nada para desfazer")
        return
    
    lista = lista.pop()
    print(f'{lista} retirada da lista')
    refazer.append(lista)

def refaz(lista,refazer):
    if not lista:
        print("nada para refazer")
        return
    tarefa = refazer.pop()
    print(f'{tarefa} refeita')
    lista.append(tarefa)
while True:
    print("listar, desfazer, refazer, sair ")
    opcao = input('digite uma tarefa ou comando: ')

    
    if opcao == 'listar': 
        
        listar(lista)
       
        continue

    elif opcao == "desfazer":
      
        desfazer(lista,refazer)
       
        continue

    elif opcao == "refazer":
     
        refaz(lista,refazer)
        
        continue

    elif opcao =="sair":
        print('FINALIZANDO')
        break
    
    else:
        adicionar(opcao,lista)
       
        continue

    
