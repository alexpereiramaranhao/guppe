"""
Já foi uma função integrada, mas a partir do Python3, reduce deixou de ser função integrada (built-in). Agora temos
que importar o módulo "functools".

Utilize a função reduce se realmente precisa delas. 99% das vezes um loop for é mais legível

Funcionamento:
Na lista, pega o primeiro e o segundo valor, manda para a função, pega o resultado e devolve para a função junto com o
terceiro valor, pega o resultado e manda novamente para a função junto com o quarto valor e assim por diante.
"""
import functools

valores = [1, 3, 4, 5, 9, 8, 1, 5]


def soma(val1, val2):
    return val1 + val2


resultado = functools.reduce(soma, valores)

print(resultado)

resultado = functools.reduce(lambda val1, val2: val1 + val2, valores)

print(resultado)

