import json
CAMINHO_DO_ARQUIVO = 'c:\\Users\\A899160\\projeto\\seccao5\\exercicio1.json'
class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome 
        self.idade = idade 
    

    
p1 = Pessoa('João', 33)
p2 = Pessoa('Helena', 21)
p3 = Pessoa('Joana', 11)
bd = [vars(p1), p2.__dict__, vars(p3)] #podemos usar tando o vars, quanto o __dict__


def fazer_dump():
    with open(CAMINHO_DO_ARQUIVO, 'w' ,encoding='utf8') as arquivo:
        print("fazendo DUMP")
        json.dump(bd,arquivo, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    print("Ele é o MAIN")
    fazer_dump()