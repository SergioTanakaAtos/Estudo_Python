

class MyError(Exception):
    ...


class OtherError(Exception):
    ...

def levantar():
    exception_ = MyError("A mensagem do meu erro")
    exception_ .add_note("voce errou isso")
    raise exception_

try:
    levantar()
except MyError as error:
    print(error.__class__.__name__)
    print(error)
    print()
    exception_ = OtherError("A mensagem do meu outro erro")
    exception_.add_note("mais uma nota")
    exception_.__notes__ += error.__notes__.copy()
    raise exception_ from error   