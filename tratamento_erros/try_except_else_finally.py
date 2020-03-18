"""
Para cada except, posso ter um else, que será executado, somente de não entrar na cláusula "except"
"""

try:
    numero = int(input("Informe um número: "))
except ValueError as value_error:
    print(f"Valor incorreto. {value_error}")
else:
    print(f"Número digitado: {numero}")
finally:
    print("remove recursos.")

