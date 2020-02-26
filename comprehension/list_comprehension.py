"""
Utilizando List comprehension, podemos gerar outras listas com dados processados a partir de outro iterável
"""

numeros = [1, 2, 3, 4, 5]

resultado = [numero * 10 for numero in numeros]

print(resultado)

# adicionando condições

impares = [numero for numero in numeros if numero % 2]
print(impares)

pares = [numero for numero in numeros if not numero % 2]
print(pares)
