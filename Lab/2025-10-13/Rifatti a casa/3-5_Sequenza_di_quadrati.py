import g2d
from Packages.g2d import init_canvas

CANVAS_W, CANVAS_H = 500, 500
g2d.init_canvas((CANVAS_W, CANVAS_H))

n = int(input("Numero di quadrati da disegnare: "))

step_l = (CANVAS_W / n - CANVAS_W) / max(n - 1, 1)
step_green = 255 / max(n - 1, 1)

for i in range(n):
    green = i * step_green
    g2d.set_color((0, green, 0))

    side = CANVAS_W + step_l * i
    g2d.draw_rect((0, 0), (side, side))

    print(f"{green: = .2f}, {side: = .2f}")

g2d.main_loop()