from math import sin, pi
import g2d
from random import choice

CANVAS_W, CANVAS_H = 400, 400

class OscillatingGhost:
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y

        self._a = 10
        self._p = 80
        self._y0 = self._y

        self._w = 20
        self._h = 20

        self._dx = 2
        self._visible = True

    def move(self):
        y = self._y0 + self._a * sin(self._x * 2 * pi / self._p)

        self._x = (self._x + self._dx) % CANVAS_W
        self._y = y % CANVAS_H

        if self._x % 20 == 0:
            change = choice([True, False, False])
            if change:
                self._visible = not self._visible

    def pos(self):
        return self._x, self._y

    def size(self):
        return self._w, self._h

    def sprite(self):
        if self._visible:
            return 20, 0
        else:
            return 20, 20

def tick():
    g2d.clear_canvas()
    g2d.draw_image("sprites.png", ghost.pos(), ghost.sprite(), ghost.size())

    ghost.move()

def main():
    global ghost
    ghost = OscillatingGhost(200, 200)

    g2d.init_canvas((CANVAS_W, CANVAS_H))
    g2d.main_loop(tick)

if __name__ == '__main__':
    main()