import g2d
from Packages.g2d import init_canvas

CANVAS_W, CANVAS_H = 500, 500
g2d.init_canvas((CANVAS_W, CANVAS_H))

n = int(input("Numero di quadrati da disegnare: "))

margin = 10

width = CANVAS_W - 2 * margin
step_x = (width - width/ n) / max(n - 1, 1)
step_side = (width / n - width) / max(n - 1, 1)
step_green = 255 / max(n - 1, 1)

for i in range(n):
    green = i * step_green
    g2d.set_color((0, green, 0))
    x = step_x * i + margin

    side = width + step_side * i
    g2d.draw_rect((x, margin), (side, side))

    print(f"{x:=.2f}, {side:.2f}")

g2d.main_loop()