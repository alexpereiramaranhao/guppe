"""
O bloco try/except

Utilizamos para tratar erros que podem ocorrer no código, permitindo assim que o programa quebre e o usuário
receba mensagens de erros inesperados.
"""

try:
    geek()
except TypeError as type_err:
    print(f"TypeError. {type_err}")
except NameError as name_err:
    print(f"NameError error. {name_err}")

