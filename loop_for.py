"""
Loop for
"""
nome = "Alex Pereira Maranhão"
lista = [1, 5, 65, 4, 78]
numeros = range(1, 10)

# itera sobre um string
for letra in nome:
    print(letra)

# itera sobre uma lista
for numero in lista:
    print(numero)

# itera sobre um range
for numero in numeros:
    print(numero)


# interando sobre o índice

for indice, valor in enumerate(nome):  # o índice pode ser _ para ser descartado.
    print(valor, end="")

