
from collections import Counter

lista = "inserir lista"

contador = Counter(lista)

for x in lista:
    if x not in contador:
        dicionario[x] = 1

    else:
        contador[x] += 1

print(dicionario.items())

print(contador.most_common(10))
