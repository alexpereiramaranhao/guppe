"""
Tuplas diferenciadas onde informamos nome e parâmetros
"""
from collections import namedtuple

# declarações
cachorroTuple = namedtuple("cachorro", "nome raca idade")
cachorroTuple = namedtuple("cachorro", "nome, raca, idade")
cachorroTuple = namedtuple("cachorro", ["nome", "raca", "idade"])

rex = cachorroTuple(idade=2, nome="Rex", raca="pitbull")
print(rex.idade)
