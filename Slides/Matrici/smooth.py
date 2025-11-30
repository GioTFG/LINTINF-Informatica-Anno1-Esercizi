"""
FUNZIONE DI SMOOTH
- Scrivere una funzione smooth
    - Parametro: matrice iniziale, di float
    - Risultato: nuova matrice con smooth
- Smooth: per ogni cella in matrice iniziale
    - Il risultato è la media dell'intorno
    - 5 valori: cella stessa e 4 adiacenti
- Attenzione alle celle esterne
    - Sommare e contare solo i valori disponibili
    - 4 valori ai bordi, 3 valori agli angoli
- Verificare la funzione con alcune matrici di test
- Fornire due implementazioni
    - Matrice in lista semplice
    - Matrice in lista di liste
"""
from sys import float_info


def smooth_flat(mat: list[float], width: int, height: int) -> list[float]:
    new_mat = [-1] * (width * height)

    for y in range(height):
        for x in range(width):
            i = y * width + x

            adjs = []
            for dx, dy in ((0, -1), (1, 0), (0, 1), (-1, 0)):
                adj_x, adj_y = x + dx, y + dy
                if 0 <= adj_x < width and 0 <= adj_y < height:
                    adjs.append(mat[adj_y * width + adj_x])

            new_mat[i] = sum(adjs) / len(adjs)
    return new_mat

def deep_smooth(mat: list[list[float]]) -> list[list[float]]:
    w, h = len(mat[0]), len(mat)

    new_mat = []
    for y, row in enumerate(mat):
        new_row = []
        for x, col in enumerate(row):
            adjs = []
            for dx, dy in ((0, -1), (1, 0), (0, 1), (-1, 0)):
                adj_x, adj_y = x + dx, y + dy
                if 0 <= adj_x < w and 0 <= adj_y < h:
                    adjs.append(mat[adj_y][adj_x])

            new_row.append(sum(adjs) / len(adjs))
        new_mat.append(new_row)
    return new_mat

flat_m = [
    1,  2,  3,  4,
    5,  6,  7,  8,
    9,  10, 11, 12,
    13, 14, 15, 16
]
new_flat_m = smooth_flat(flat_m, 4, 4)

print("Flat list")
for y in range(4):
    for x in range(4):
        term = "\n" if x == 3 else ""
        print(f"{new_flat_m[y * 4 + x]: 10.2f}", end= term)

deep_m = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
new_deep_m = deep_smooth(deep_m)

print("List of lists")
for y in range(4):
    for x in range(4):
        term = "\n" if x == 3 else ""
        print(f"{new_deep_m[y][x]: 10.2f}", end= term)