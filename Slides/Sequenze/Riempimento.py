"""
RIEMPIMENTO
- Definire una funzione fill con due parametri
    - Lista di numeri interi
    - Indice intero i: una posizione nella lista
- Riempie con valori 1 le celle che contengono inizialmente 0, attorno all'indice dato
    - Elemento con indice i ≠ 0: termina subito
    - Elemento con indice i = 0: impostato a 1, riempimento a destra e sinistra
    - Arrivati a elemento ≠ 0: riempimento si blocca
- Es.: apice indica posizione i nella lista: avvio del riempimento
"""

def fill(l: list[int], i: int):
    stop = False
    i_left, i_right = i, i+1
    while not stop:
        right_stopped = False
        left_stopped = False

        if i_left >= 0 and l[i_left] == 0:
            l[i_left] = 1
            i_left -= 1
        else:
            left_stopped = True

        if i_right < len(l) and l[i_right] == 0:
            l[i_right] = 1
            i_right += 1
        else:
            right_stopped = True

        if left_stopped and right_stopped:
            stop = True


l = [0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0]
fill(l, 9)
print(l)