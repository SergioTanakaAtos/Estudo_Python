def criar_multiplicador(multi):
    def multiplicar(num):
        return num * multi
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2))

