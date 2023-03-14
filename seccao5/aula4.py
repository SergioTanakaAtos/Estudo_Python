 
class Cliente():
    def __init__(self,nome):
        self.nome = nome 
        self.enderecos =[]
    
    def inserir_enderecos(self,rua,numero):
        self.enderecos.append(Endereco(rua,numero))
    
    def inserir_enderecos_externos(self,enderecos):
        self.enderecos.append(enderecos)

    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua,endereco.numero)
    
    def __del__(self):
        print('APAGANDO,', self.nome) 



class Endereco:
    def __init__(self,rua,numero):
        self.rua = rua 
        self.numero = numero 
    
    def __del__(self):
        print('APAGANDO,', self.rua, self.numero)


cliente1 = Cliente("sergio")


        