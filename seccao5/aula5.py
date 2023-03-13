from abc import ABC, abstractmethod

class Notificacao:
    def __init__(self,mensagem) -> None:
        self.mensagem = mensagem 

    @abstractmethod
    def enviar(self) -> bool:
        ...
    
class NotificacaoEmail(Notificacao):

    def enviar(self):
        print("E-mail - envinado", self.mensagem)
        return True

class NotificacaoSMS(Notificacao):

    def enviar(self):
        print("SMS - envinado", self.mensagem)
        return True
        
    
def notificar(notificacao: str):
    notificacao_enviada = notificacao.enviar()

    if notificacao_enviada:
        print("notificacao enviada")
    else:
        print("NOtificacao nao enviada")
    


notificacao_email = NotificacaoEmail("testando e_mail")
notificar(notificacao_email)


notificacao_sms = NotificacaoSMS("testando SMS")
notificar(notificacao_sms)

