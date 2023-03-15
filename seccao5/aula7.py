# dataclasses - O que são dataclasses?
# O módulo dataclasses fornece um decorador e funções para criar métodos como
# __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo
# usuário.
# Em resumo: dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
# doc: https://docs.python.org/3/library/dataclasses.html
from dataclasses import dataclass,asdict,astuple,field


@dataclass
class Pessoa:
    nome: str
    sobrenome: str 
    enderecos: list[str] = field(default_factory=list)
    def __post_init__(self):
        return f'{self.nome} {self.sobrenome}'


    @property
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome} POST INIT'
    
    @nome_completo.setter
    def nome_completo(self,valor):
        nome, *sobrenome = valor.split()
        self.nome = nome 
        self.sobrenome = ''.join(sobrenome)

if __name__ == '__main__':
    p1 = Pessoa('Sergio','Tanaka')
    print(p1)
    print(asdict(p1))
    print(astuple(p1))
    print(p1.nome_completo)