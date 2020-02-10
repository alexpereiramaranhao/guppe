"""
Escopo de variáveis
- Variáveis globais
    * escopo de todo o programa
- Variáveis locais
    * reconhecidas somente no bloco

Declaração em Python:

nome_variavel = valor_variavel

Python tem tipagem dinâmica, seu valor é inferido na atribuição.
"""

numero = 42  # variável global

print(type(numero))

if numero > 10:
    novo = numero+10  # Escopo local
    print(novo)

print("Valor novo " + str(novo+1))
