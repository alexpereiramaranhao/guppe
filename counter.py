"""
Múdule Collection - Counter
Collection - Hight Performance Container Datetypes

Recebe um interável como argumento e cria um objeto  Collection Counter. Parce com um dicionário, que recebe como chave
 o intem passao e como valor a quantidade de ocorrências do elemento.
"""
from collections import Counter

lista = [1, 2, 3, 1, 1, 1, 2, 6, 7, 7, 3, 8, 9, 5, 12, 1]

resultado = Counter(lista)
print(type(resultado))
print(resultado)

print("--------------------------")

print(Counter("Alex Pereira Maranhão"))

texto = """A Wikipédia é um projeto de enciclopédia colaborativa, universal e multilíngue estabelecido na internet sob o
 princípio wiki. Tem como propósito fornecer um conteúdo livre, objetivo e verificável​​, que todos possam editar e
 melhorar. O projeto é definido pelos princípios fundadores. O conteúdo é disponibilizado sob a licença Creative
 Commons BY-SA e pode ser copiado e reutilizado sob a mesma licença — mesmo para fins comerciais — desde que
 respeitando os termos e condições de uso."""

palavras = texto.split()
resultado = Counter(palavras)

print(resultado)
print(resultado.most_common(5))



