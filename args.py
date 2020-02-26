"""
Entendendo o *args
    - É um parâmetro, como outro qualquer;
    - Pode chamá-lo de qualquer nome, desde que inicie com *
        - Por convenção, utiliza-se o *args
    - Guarda os valores de entrada em uma tupla
"""


def somar_numeros(*args):
    return sum(args)


print(somar_numeros(1, 2))
print(somar_numeros(1, 2, 3))
print(somar_numeros(1, 2, 4, 2))

"""desempacotador -  o * informa ao Python que estamos passando com argumento, uma coleção de dados, assim, entende
que precisa desempacotar os dados"""
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(somar_numeros(*numeros))
