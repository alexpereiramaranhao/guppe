"""
Expressões lambdas são funções sem nome, ou seja, funções anônimas.

Geralmente utiliza para fazer ordenação e filtragem, mas não se limitam a isso.

"""

# em Python


def soma(a, b):
    return a + b


print(soma(2, 2))


# expressão lambda (modo ruim)


result = lambda a, b: a + b

print(result(2, 2))

# outro exemplo

autores = ["Isaac Asimov", "Ray Brandbury", "Paulo C. Coelho", "Alex P. Maranhão"]

print(autores)

autores.sort(key=lambda sobrenome: sobrenome.split(" ")[-1].lower())

print(autores)