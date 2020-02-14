"""
Ranges são utilizados para gerar sequências numéricas, não de forma aleatório,
mas sim de maneira específicada.

OBS.: Valor de parada não inclusive (início padrão em 0 e passo de 1 em 1)
"""

for num in range(11):
    print(f"{num}-", end="")

print("\n--------Com valor de início-------------")

for num in range(1, 11):
    print(f"{num}-", end="")

print("\n--------Com valor de incremento-------------")

for num in range(1, 11, 2):
    print(f"{num}-", end="")

print("\n--------Com valor de incremento (inverso)-------------")

for num in range(10, 1, -1):
    print(f"{num}-", end="")
