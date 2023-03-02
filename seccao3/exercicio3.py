lista = [1,3,2,2,1]
indices = range(len(lista))
lista_enumerada = enumerate(lista)
#for i in indices:
    #print(i)
for i in lista_enumerada:
    print(i)



#desenpacotamento
_, nome,*_ = [1,2,4,5,6]
print(nome,)
for i, numero in enumerate(lista):
    print(i,numero)

