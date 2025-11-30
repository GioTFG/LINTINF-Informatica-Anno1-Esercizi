"""
CLAMP DI LISTA
- Definire la funzione clamp con tre parametri
    - Una lista di numeri
    - Un limite inferiore a
    - Un limite superiore b
- Modifica numeri nella lista
    - Se minori di a, li sostituisce con a
    - Se maggiori di b, li sostituisce con b
"""

def clamp(l: list[int], a: int, b: int):
    for i, v in enumerate(l):
        if v < a:
            l[i] = a
        if v > b:
            l[i] = b

data = [3, 4, 6, 7, 3, 5, 6, 12, 4]
print(data)
clamp(data, 5, 10)
print(data)