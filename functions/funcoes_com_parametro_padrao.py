"""
Funções onde a passagem de parâmetros é opcional
- print() é opcional
- para se tornar valor opcional, atribuimos valor à declaração do parâmetro
"""

# valores default devem ficar no fianl


def exponencial(numero, potencia=2):
    return numero ** potencia


print(exponencial(2))
print(exponencial(2, 3))

# funções como parâmetros


def soma(parcela1, parcela2):
    return parcela1 + parcela2


def subtracao(parcela1, parcela2):
    return parcela1 - parcela2


def matematica(valor1, valor2, funcao=soma):
    return funcao(valor1, valor2)


print(matematica(2, 3, subtracao))

# Escopo de variáveis

total = 0


def incremente():
    global total  # queremos usar a variável global e não uma local

    total += 1

    return total


print(incremente())
