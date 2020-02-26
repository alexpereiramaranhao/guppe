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

# forma mais comum de declarar

conjunto = {1, 2, 3, 3,  3, 4, 7, 9}

print(type(conjunto))
print(conjunto)

if 3 in conjunto:
    print("número encontrado.")

conjunto.add(10)
print(conjunto)

conjunto.remove(10)  # caso não seja encontrado, gera excecão KeyError
conjunto.discard(10)  # caso não seja encontrado, não gera erro
print(conjunto)

lista = ["Goiânia", "São Paulo", "Cuiabá", "Anápolis", "Goiânia", "Goiânia"]
print(f"Quantidade de usuários {len(lista)}")
print(f"Cidades participantes {set(lista)}")

print("-----------------------------------------------------")

# Métodos matemáticos dos conjuntos

pythonSet = {"Marcos", "Alex", "Júlia", "Antônio"}
javaSet = {"Alex", "Fernando", "Júlia", "Guthierrez", "Diogo"}

# Gerar um conjunto de nomes únicos
alunosUnicos = pythonSet.union(javaSet)
print(alunosUnicos)
alunosUnicos = pythonSet | javaSet
print(alunosUnicos)

# só estuda em um
alunosUnicos3 = pythonSet.difference(javaSet)
print(alunosUnicos3)

# estuda em ambos
alunosUnicos4 = pythonSet.intersection(javaSet)
print(alunosUnicos4)
alunosUnicos4 = pythonSet & javaSet
print(alunosUnicos4)

