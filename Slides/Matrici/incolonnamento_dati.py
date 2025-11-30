r"""
INCOLONNAMENTO DATI
- Visualizzare due tabelle con i caratteri ASCII
    - 4 righe x 24 colonne, codici da 32 a 126
Tabella 1: mostrare in ordine i caratteri, colonna per colonna
Tabella 2: mostrare in ordine i caratteri, riga per riga

 $(,048<@DHLPTX\`dhlptx|
!%)-159=AEIMQUY]aeimquy}
"&*.26:>BFJNRVZ^bfjnrvz~
#'+/37;?CGKOSW[_cgkosw{

Usare sempre due cicli for annidati: esterno su y, interno su x
In ogni posizione, calcolare il carattere da visualizzare: x * ROWS + y...
"""

ROWS, COLS = 4, 24

print("Per colonne")
for y in range(ROWS):
    for x in range(COLS):
        i = y + x * ROWS
        term = "\n" if x == COLS - 1 else ""
        print(chr(i + 32), end= term)
print()
print("Per righe")
for y in range(ROWS):
    for x in range(COLS):
        i = y * COLS + x
        term = "\n" if x == COLS - 1 else ""
        print(chr(i + 32), end= term)