"""
Definindo uma função

def nome_funcao(parametros):
    bloco da função

def -> definition. Informa ao Python que está sendo declarado uma função
- Nome da função: sempre letra minúscula e separadas por underline (snake_case)
- Parâmetros separados por vírgula, podendo ser opcionais ou não
- A função pode ou não ter retorno
"""
nome = "Alex Pereira Maranhão"

def funcao_teste(nome):
    print(nome)


funcao_teste(nome)


# É possível criar variáveis do tipo da função e executar a função através da variável

teste = funcao_teste

teste(nome)
