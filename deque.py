"""
É uma lista de alta performance
"""

from collections import deque

deque = deque("Alex Pereira Maranhão")
print(deque)

# manipula tanto a ponto quanto o final da lista
deque.appendleft("J")
print(deque)

letra = deque.popleft()
print(deque)
print(letra)
