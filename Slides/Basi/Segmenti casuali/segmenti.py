import g2d
from random import randrange

numero_segmenti = int(g2d.prompt("Quanti segmenti disegnare? "))

dimensioni_canvas = (500, 500)
g2d.init_canvas(dimensioni_canvas)

g2d.set_color((0, 0, 0))
for i in range(numero_segmenti):
    g2d.draw_line((randrange(dimensioni_canvas[0]), randrange(dimensioni_canvas[1])), (randrange(dimensioni_canvas[0]), randrange(dimensioni_canvas[1])))

g2d.main_loop()