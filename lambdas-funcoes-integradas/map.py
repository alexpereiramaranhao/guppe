"""
! Não são dictionary (mapas)

Com Map, fazemos o mapeamento de valores para a função.
"""
import math


def area(raio):
    return math.pi * (raio ** 2)


print(area(2))

raios = [2, 3, 5, 32.2, 5, 6]

# calcular as áreas de uma forma comum

areas = []
for raio in raios:
    areas.append(area(raio))

print(areas)

"""
Utilizando Map.
Map é uma função que recebe dois parâmetros, sendo o primeiro uma função e o segundo um iterável. Retorna um MapObject
"""

areas = map(area, raios)
print(areas)
print(type(areas))
print(list(areas))

# Utilizando lambda

print(list(map(lambda r: area(r), raios)))

# outro exemplo

cidades = [("Berlim", 18), ("Rio de Janeiro", 32), ("Goiânia", 28)]

print(list(map(lambda dado: (dado[0], (9/5)*dado[1]+32), cidades)))


