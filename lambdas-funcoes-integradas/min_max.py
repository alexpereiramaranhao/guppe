"""
max() e min - retorna o maior/menor valor em um iteravel ou o maior/menor de dois ou mais elementos
"""

lista = [1, 5, 9, 5, 1, 0, 5, 7, 3]
print(max(lista))

tupla = (1, 65, 6, 5, 8, 89)
print(max(tupla))

conjunto = {1, 5, 8, 65, 78}
print(max(conjunto))

print(max(1, 2))

nomes = ["Alex", "Maria", "Juliana", "Alessandra"]

print(max(nomes))

print(max(nomes, key=lambda nome: len(nome)))
print(min(nomes, key=lambda nome: len(nome)))
