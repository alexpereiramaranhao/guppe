"""
unários: not
binários: and, or, is
"""

ativo = True
logado = True
if logado is True:  # Redundante, mas é só para teste :-)
    print("Logado!")

if ativo and logado:
    print("Bem vindo")
elif ativo and not logado:
    print("Favor, fazer login.")
elif not ativo:
    print("Por favor, ativar sua conta")

