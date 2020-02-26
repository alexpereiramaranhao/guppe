"""
**kwargs

Por convenção, o nome a se adotar é "kwargs".
- O **kwargs exige que informemos parâmetros nomeados para transformar em um dicionário.
- São parâmetros não obrigatórios
- Nas nossas funções, podemos ter, NESSA ORDEM:
    - Parâmetros obrigatórios;
    - *args
    - Parâmetros não obrigatórios (default)
    - **kwargs
"""


def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f"{pessoa.title()} gosta de {cor}")


cores_favoritas(alex="verde", alessandra="rosa", henrique="azul")

# sequencia de parâmetros da funnção


def funcao_exemplo(nome, idade, *args, solteiro=False, **kwargs):
    print(f"{nome} tem {idade}")

    print(args)

    if solteiro:
        print("Solteiro")
    print("Casado")

    print(kwargs)


funcao_exemplo("Alex", 31)
funcao_exemplo("Alessandra", 29, 4, 5, 6, solteiro=False)
funcao_exemplo("Henrique", 2, eu="Não", voce="Vai")
funcao_exemplo("Giovanna", 29, 4, 5, 6, java=False, python=False)


# desempacotar
def mostrar_nome(**kwargs):
    print(kwargs)


nomes = {"nome": "Alex", "sobrenome": "Pereira Maranhão"}

print(mostrar_nome(**nomes))
