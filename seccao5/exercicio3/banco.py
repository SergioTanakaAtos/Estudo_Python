import pessoas 
import conta 

class Banco():
    def __init__(self,
        agencias:list[int] | None = None ,
        clientes:list[pessoas.Pessoa] | None= None,
        contas:list[conta.Conta] | None = None ):

        self.agencias = agencias or []
        self.clientes = clientes or []
        self.conta = contas or []
    

    def _checa_agencia(self,conta):
        if conta.agencia in self.agencias:
            print("_checa_agencia", True)
            return True 
        print("_checa_agencia", False)
        return False

    def _checa_cliente(self,cliente):
           if cliente in self.clientes:
                print("_checa_cliente", True)
                return True 
           print("_checa_cliente", False)
           return False

    def _checa_conta(self,conta):
        if conta in self.conta:
            print("_checa_conta", True)
            return True 
        print("_checa_conta", False)
        return False
    
    def _checa_conta_cliente(self,conta,cliente):
        if conta is cliente.conta:
            print("_checa_conta_cliente", True)
            return True 
         
        print("_checa_conta_cliente", False)
        return False


    def autenticar(self,cliente:pessoas.Pessoa, conta:conta.Conta):
        return self._checa_agencia(conta) and \
        self._checa_cliente(cliente) and \
        self._checa_conta(conta) and \
        self._checa_conta_cliente(cliente,conta)
    

    def __repr__(self):
        class_name = type(self).__name__ 
        attrs = f'({self.agencias!r}, {self.clientes!r}, {self.conta!r}'
        return f"{class_name} {attrs}"

if __name__ == "__main__":
    c1 = pessoas.Cliente("sergio", 18)
    cc1 = conta.ContaCorrente(111,222,0,0)
    c1.conta = cc1 

    c2 = pessoas.Cliente('Maria', 18)
    cp1 = conta.ContaPoupanca(112, 223, 100)
    c2.conta = cp1

    banco = Banco()

    banco.clientes.extend([c1,c2])
    banco.conta.extend([cc1,cp1])
    banco.agencias.extend([111,222])

