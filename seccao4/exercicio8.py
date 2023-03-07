lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
lista_soma = []
soma_python = [x + y for x,y in zip(lista_a,lista_b)]
print(soma_python)
def somar(l1,l2):
    intervalo = min(len(l1), len(l2))
    for i in range(intervalo):
        lista_soma.append(l1[i] + l2[i])
    return lista_soma

# print(somar(lista_a,lista_b))