"""
Recebendo dados do usuário
- input() sempre devolve uma string
String:
    'Alex'
    "Alex"
    '''Alex'''
    aspas duplas tripla
"""
# Versão antiga
# Recebendo dados
nome = input("Qual o seu nome? ")

# Saída de dados
print('Seja bem vindo %s ' % nome)

# Recebendo dados
print("Qual a sua idade?")
idade = int(input())

# Saída de dados
print('%s você tem %s anos' % (nome, idade))


# Versão mais atual
print('{0} você tem {1} anos'.format(nome, idade))

# Versão moderna
print(f'{nome} você tem {idade} anos')

# Cast
print(f'Você nasceu em {2020 - int(idade)}')
