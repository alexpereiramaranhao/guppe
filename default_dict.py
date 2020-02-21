"""
Não apresenta KeyErro - informamos um valor default.
Caso tentar acessar uma chave inexistente, essa chave será criada com o valor default
"""
from collections import defaultdict

dicionario = defaultdict(lambda: 0)

dicionario["curso"] = "Python"
print(dicionario)
print(dicionario["outro"])
print(dicionario)

