import random, g2d

dimensioni_canvas = (500, 500)
g2d.init_canvas(dimensioni_canvas)

n = int(g2d.prompt("Inserire il numero di quadrati da disegnare: "))

for n in range(n):
    g2d.set_color((random.randrange(256), random.randrange(256), random.randrange(256)))
    g2d.draw_rect((random.randrange(399), random.randrange(399)), (100, 100))

g2d.main_loop()