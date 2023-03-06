from dados import produtos


import copy


novos_produtos = [
    {
    **p, 'preco' : round(p['preco'] *1.1,2)
     }

    for p in copy.deepcopy(produtos)
]

produtos_de_forma_odenada = sorted(
    copy.deepcopy(produtos),
    key = lambda p:p['nome']
)


preco_crescente = sorted(
    copy.deepcopy(produtos),
    key = lambda p: p['preco']
)

print(produtos, sep= '\n')
print()
print(preco_crescente, sep= '\n')


