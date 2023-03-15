from abc import ABC, abstractmethod

class Conta():
    def __init__(self,agencia: int ,conta: int ,saldo: float =0 )-> None:
        self.agencia = agencia
        self.saldo = saldo 
        self.conta = conta 
    
    @abstractmethod
    def sacar(self,valor):
        ...
    
    def depositar(self,valor)->float:
        self.saldo += valor
        print(f"O valor depositado foi de {valor}, saldo total {self.saldo}")

    def ver_saldo(self, msg = '')->None :
        print(f"Saldo de:{self.saldo} {msg}")

    def __repr__(self):
        class_name = type(self).__name__ 
        attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r},'
        return f"{class_name} {attrs}"
    

class ContaPoupanca(Conta): 
    def sacar(self, valor):
        saque = self.saldo - valor 
        if saque >= 0:
            self.saldo -= valor
            self.ver_saldo(f'Saque:{valor}')
            return self.saldo 
        print("NAO FOI POSSIVEL SACAR")
        return self.saldo

class ContaCorrente(Conta): 
    def __init__(self, agencia: int, conta: int, saldo: float = 0, limite:float = 0 ) -> None:
        super().__init__(agencia, conta, saldo)
        self.limite = limite 

    def sacar(self, valor):
        saque = self.saldo -valor 
        limite_max = -self.limite

        if saque >= limite_max:
            self.saldo -= valor     
            self.ver_saldo(f'Saque:{valor}')
            return self.saldo 
        
        print("NAO FOI POSSIVEL SACAR")
        print(f"Seu limite e: {-self.limite}")
        self.ver_saldo(f'SAQUE NEGADO {valor}')
        return self.saldo
    
    def __repr__(self):
        class_name = type(self).__name__ 
        attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r},'\
        f'{self.limite})'
        return f"{class_name} {attrs}"
    
    
if __name__ == "__main__":
    cp1 = ContaPoupanca(111,222)
    cp1.depositar(10)
    cp1.sacar(1)


    print("*" *30)

    cc1 = ContaCorrente(111,222,0,100)
    cc1.depositar(10)
    cc1.sacar(11)
    cc1.sacar(90)
    cc1.sacar(11)
    
    