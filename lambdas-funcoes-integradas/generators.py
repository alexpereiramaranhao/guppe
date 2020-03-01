"""
Tuple Comprehension são chamados de Generators
"""

nomes = ["Alex", "Alessandra", "Henrique"]

print(any(nome.__contains__("A") for nome in nomes))

nomesComLetraA = filter(lambda nome: nome.__contains__("A"),  nomes)

print(list(nomesComLetraA))
