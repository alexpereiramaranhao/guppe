def multiplica(produto_1, produto_2):
    return produto_1 * produto_2


print(multiplica(2, 4))

# podemos retornar múltiplos valores


def multiplos_retornos():
    return 1, 2, 3


valor1, valor2, valor3 = multiplos_retornos()

print(valor1, valor2, valor3)
