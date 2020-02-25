listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(listas)

print(listas[0][1])

# iteração

for lista in listas:
    for item in lista:
        print(item)

print("---------- com comprehesion --------------")

[[print(numero) for numero in lista] for lista in listas]


