import requests

from collections import Counter

texto = requests.get("https://bit.ly/2Cu73N6").text

palavras = texto.split()

contador_palavras = Counter(palavras)
print(contador_palavras.most_common(10))
