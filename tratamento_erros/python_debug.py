"""
Debugging com PDB (Python Debugger)
É necessário importar o pacote pdb e utilizar a função set_trace(). Isso substitui a ide.
A partir do Python 3.7, pdb não é necessário mais ser inportado, virou uma built-in chamda breakpoint()
"""
import pdb


def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f"Ocorreu um erro. {err}"


print(dividir(4, 0))
