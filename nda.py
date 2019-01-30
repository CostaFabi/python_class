from collections import Counter

def contar_coisas(objeto):

    n = 10

    for x in objeto:
        if type(objeto) == type(str()):
            palavras = objeto.split()

            contador = Counter(palavras)

        elif type(objeto) == type(list()):
            contador = Counter(objeto)


    return contador.most_common(n)
