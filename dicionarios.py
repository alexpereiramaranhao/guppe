"""
- Em algumas linguagens de progamação, os dicionários Python, são conhecidos como mapas
- Dicionários são chave/valor
- São representados por chaves {}
"""
print(type({}))

paises = {"BR": "Brasil", "EUA": "Estados Unidos"}

print(paises)

print(paises["EUA"])
print(paises.get("BR"))
print(paises.get("FR"))

# Tipo sem tipo "None" - é sempre falso
pais = None

print(type(pais))

if pais:
    print(pais)
else:
    print("Sem nome")

pais = paises.get("ES", "Não encontrado")

print(pais)

paises.update({"PT": "Portugal"})

print(paises)

paisDel = paises.pop("PT")
print(paisDel)

print(paises)
