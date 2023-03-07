
#funcao decoradora 
def criar_funcao(func):
    def interna(*args, **kwargs):
        for arg in args:
            e_str(arg)
        resultado = func(*args, **kwargs)
        return resultado
    return interna

@criar_funcao #syntax sugar 
def inverte_str(string):
    print(inverte_str.__name__)
    return string[::-1]

def e_str(param):
    if not isinstance(param,str):
        raise TypeError('param deve ser uma string')

checando_parametro = criar_funcao(inverte_str)
invertida = checando_parametro("123")
print(invertida)