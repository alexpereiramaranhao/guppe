"""
O Filter serve para filtrar dados de uma determinada coleção.
"""
import statistics

valores = [1.20, 2.65, 3.98, 4.32, 5.29, 6.86]

print(f"Valores: {valores}")

media = statistics.mean(valores)

print(f"Média: {media}")

# O Filter recebe dois parâmetros, uma função e um interável

abaixoMedia = filter(lambda x: x < media, valores)
print(abaixoMedia)
print(f"Valores abaixo da média {list(abaixoMedia)}")

acimaMedia = filter(lambda x: x > media, valores)

print(f"Valores acima da média {list(acimaMedia)}")

print("--------------------------------------------------------")

paises = ["", "Brasil", "", "", "Argentina", "Colômbia", "Paraguai", ""]

res = filter(lambda pais: pais != "", paises)

print(list(res))

res = filter(None, paises)

print(list(res))

print("--------------------------------------------------------")

usuarios = [
    {"usuario": "Alex Pereira Maranhão", "tweets": ["Python é show!", "E o java?!"]},
    {"usuario": "Alessandra Ferreira", "tweets": []},
    {"usuario": "Henrique Ferreira Maranhão", "tweets": ["Carrinhos são legais!"]}
]

inativos = filter(lambda usuario: not len(usuario.get("tweets")), usuarios)

print(list(inativos))

print("--------------------------------------------------------")

nomes = ["Alex", "Alessandra", "André", "Maria", "Ana"]

nomesMaioresCincoCaracteres = list(map(lambda nome: f"instrutor {nome}", filter(lambda nome: len(nome) < 5, nomes)))

print(nomesMaioresCincoCaracteres)
