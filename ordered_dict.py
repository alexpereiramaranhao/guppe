from collections import OrderedDict

dicionario = OrderedDict({"nome": "Alex", "idade": 31, "sobrenome": "Pereira Maranhão"})
print(dicionario)

for chave, valor in dicionario.items():
    print(f"{chave}:{valor}")

