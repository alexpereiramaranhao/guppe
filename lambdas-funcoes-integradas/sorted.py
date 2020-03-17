"""
Não confundir sorted com função sort() presente em listas

Sorted serve para ordenar qualquer iterável
"""
numeros = [6, 8, 2, 3, 7]
print(numeros)

print(sorted(numeros))

print(numeros)

print(sorted(numeros, reverse=True))

print("--------------------------------------------")

usuarios = [
    {"username": "Alex", "tweets": ["Ok!", "Muito massa!"]},
    {"username": "Alessandra", "tweets": ["Onde é?", "Não dá para ser"], "cor": "Amarelo"}
]

print(sorted(usuarios, reverse=True, key=lambda usuario: usuario["username"]))


