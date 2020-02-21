"""
Refere-se à teoria de conjuntos da Matemática

- No Python os conjuntos são chamados de Sets e
    - não possuem valores duplicados
    - não possuem valores ordenados
    - elementos não acessados via índice, ou seja, não são indexados

São bons para se utilizar quando precisamos armazenar elementos e não importa a ordenação.
Não precisamos nos preocupamos com chaves, valores e itens duplicados.
São referenciados por { } e a diferença para mapas (dicionarios) é:
    - Um mapa tem chave/valor;
    - conjunto apenas valor.

"""

#  Definindo um conjunto

conjunto = set({1, 2, 3, 4, 5, 6, 7, 7})

print(type(conjunto))
print(conjunto)
