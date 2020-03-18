"""
Levantando os próprios erros com raise

raise > Lança exceções

OBS: O raise não é uma função, é uma palavra reservada, assim como def ou qualquer outra em Python.

Para simplificar, pense no raise como sendo útil para que possamos criar nossas próprias exceções e mensagens de erro.

A forma geral de utilização é:

raise TipoDoErro("Mensagem do erro")

O raise finaliza a função
"""


def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError("texto deve ser string")
    if type(cor) is not str:
        raise TypeError("cor precisa ser string")
    print(f"O texto {texto} será impresso em {cor}")


colore("texto", "azul")

