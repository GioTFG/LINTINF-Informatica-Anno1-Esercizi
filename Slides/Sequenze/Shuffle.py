"""
SHUFFLE
- Definire una funzione shuffle
    - Parametro: una lista di valori
    - Mescola in-place gli elementi della lista
- Per ogni indice i della lista
    - Genera un indice j casuale, valido
    - Scambia di posto elementi in i e j

Naturalmente, senza usare la funzione random.shuffle
"""
from random import randrange


def shuffle(l: list):
    for i, v in enumerate(l):
        j = randrange(len(l))
        l[i], l[j] = l[j], l[i]

list1 = ["Mela", "Pera", "Banana", "Caffè"]
print(list1)
shuffle(list1)
print(list1)