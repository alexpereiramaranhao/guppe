"""
Listas em Python são arrays, são DINÂMICOS e aceitam QUALQUER TIPO de dados
    - São representadas por []
"""
lista1 = [1, 3, 6, 2, 5, 9, 7, 1, 0, 6, 8, 1]

lista2 = ["A", "l", "e", "x", 1]

lista3 = []

lista4 = list(range(11))

lista5 = list("Alex")

num = 8

print("--------------- tem item na lista?--------------------------")

if num in lista1:
    print(f"O numero {num} ESTÁ na lista")
else:
    print(f"O numero {num} NÃO ESTÁ na lista")

print("--------------- sort da lista--------------------------")

lista1.sort()
print(lista1)

lista5.sort()
print(lista5)

print(lista1.count(1))

print("--------------- adicionar elementos na lista--------------------------")
# utilizamos a função append (um elemento por vez)

print(lista1)
lista1.append(7)
print(lista1)
lista1.pop(1)
print(lista1)
lista1.append(list(range(4)))  # coloca como novo item
print(lista1)
lista1.extend(list(range(4)))  # agrega aos itens da lista e pode ser somente um argumento iterável.
print(lista1)

print("--------------- adicionar elementos na lista, determinada posição--------------------------")

lista1.insert(0, "Novo valor")
print(lista1)

lista1.reverse()
print(lista1)

print(lista1[::-1])

print("--------------- tamanho da lista--------------------------")

print(len(lista1))

print("--------------- remove elemento da lista--------------------------")

print(lista1)
lista1.pop()  # sempre remove o último
print(lista1)

print(lista1)
lista1.pop(4)  # sempre remove o último
print(lista1)

print("--------------- remove tudo da lista--------------------------")

print(lista1)
lista1.clear()  # sempre remove o último
print(lista1)

print("--------------- split string --------------------------")

nome = "Alex Pereira Maranhão"
listaNomes = nome.split()
print(listaNomes)

print("--------------- lista para string --------------------------")

listaNomes = ["Alex", "Pereira", "Maranhão"]
print(" ".join(listaNomes))

print("--------------- iterando --------------------------")

print(lista4)
for elemento in lista4:
    print(f"{elemento}")

print(listaNomes[-1])

print("--------------- índices --------------------------")
for indice, valor in enumerate(listaNomes):
    print(indice)

# Pega o índice do valor. Se não existir dá "ValueError"
print("index >", listaNomes.index("Alex"))

print("--------------- soma valores --------------------------")

numeros = [1, 2, 3, 4, 5, 59, 6, 8, 7, 9, 11, 25, 45]

print(sum(numeros))
print(max(numeros))
print(min(numeros))
print(len(numeros))
