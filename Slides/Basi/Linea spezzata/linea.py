import g2d
from random import randrange

numero_segmenti = int(g2d.prompt("Inserire il numero di segmenti della spezzata:"))

dimensioni_canvas = (500, 500)
g2d.init_canvas(dimensioni_canvas)

while numero_segmenti < 1:
    g2d.prompt("Inserire un numero valido di segmenti:")

punto_partenza = (randrange(dimensioni_canvas[0]), randrange(dimensioni_canvas[1]))
g2d.set_color((0, 0, 0))

for i in range(numero_segmenti):
    punto_arrivo = (randrange(dimensioni_canvas[0]), randrange(dimensioni_canvas[1]))
    g2d.draw_line(punto_partenza, punto_arrivo)
    punto_partenza = punto_arrivo

g2d.main_loop()