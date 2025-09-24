import g2d
from random import randrange

numero_quadrati = int(g2d.prompt("Quanti quadrati inserire? "))

while numero_quadrati < 1 or numero_quadrati > 500:
    numero_quadrati = int(g2d.prompt("Quanti quadrati inserire (max. 500)? "))

dimensioni_canvas = (500, 500)
g2d.init_canvas(dimensioni_canvas)

lato = 500 / numero_quadrati

for i in range(numero_quadrati):
    g2d.set_color((randrange(256), randrange(256), randrange(256)))
    g2d.draw_rect((i * lato, i * lato), (lato, lato))

g2d.main_loop()