"""
ISTOGRAMMA CON BARRE ORIZZONTALI
- Chiedere all'utente una lista di valori positivi
    - Fino a inserimento del valore 0 (sentinella)
- Mostrare un istogramma
    - Lunghezza orizzontale di ciascuna barra proporzionale al valore corrispondente
    - La barra più lunga occupa tutto lo spazio disponibile in orizzontale.
"""

import Packages.g2d as g2d

W, H = 400, 300

g2d.init_canvas((W, H))

vals = []
# while (num := int(input("Inserire un numero (0 per terminare): "))) > 0:
while (num := int(g2d.prompt("Inserire un numero (0 per terminare): "))) > 0:
    vals.append(num)

max_val = max(vals)
delta_y = H / len(vals)

y = 0
for i, v in enumerate(vals):
    g2d.set_color((50, 50, 200))
    g2d.draw_rect((0, y), (v / max_val * W, delta_y))
    y += delta_y

    g2d.set_color((0, 0, 0))
    g2d.draw_text(str(v), (v / max_val / 2 * W, y + delta_y / 2), 3)

g2d.main_loop()