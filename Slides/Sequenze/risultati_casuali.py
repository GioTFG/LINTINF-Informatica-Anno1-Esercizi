"""
RISULTATI CASUALI
- Simulare n lanci di una coppia di dadi
    - n scelto dall'utente
- Contare quante volte si presenta ciascun risultato
    - Risultati possibili tra 2 e 12
    - Somma dei due dadi
"""
from random import randint

occurrences = [0] * 11 # Numbers from 2 to 12. The number matches the index shifted by 2

n = int(input("Inserire il numero di lanci da simulare: "))
for _ in range(n):
    dice1, dice2 = randint(1, 6), randint(1, 6)

    occurrences[dice1 + dice2 - 2] += 1

for i, v in enumerate(occurrences):
    print(f"{i + 2: 3}: {v: 3} times.")