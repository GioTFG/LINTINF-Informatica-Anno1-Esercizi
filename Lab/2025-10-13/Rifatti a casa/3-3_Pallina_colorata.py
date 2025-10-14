from random import randrange

import g2d

CANVAS_W, CANVAS_H = 500, 500
BALL_W, BALL_H = 20, 20

class Ball:
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y
        self._dx = 4
        self._dy = 4

        self.change_color()

    def move(self):
        if not 0 <= self._x + self._dx <= CANVAS_W - BALL_W:
            self._dx = -self._dx
            self.change_color()
        if not 0 <= self._y + self._dy <= CANVAS_H - BALL_H:
            self._dy = -self._dy
            self.change_color()

        self._x += self._dx
        self._y += self._dy

    def pos(self) -> tuple[int, int]:
        """
        :return: Restituisce la posizione (x,y) nel canvas della pallina.
        """
        return self._x, self._y

    def change_color(self):
        self._red = randrange(255)
        self._green = randrange(255)
        self._blue = randrange(255)

    def color(self) -> tuple[int, int, int]:
        return self._red, self._green, self._blue

def tick():
    g2d.clear_canvas()
    g2d.set_color(b1.color())
    g2d.draw_rect(b1.pos(), (BALL_W, BALL_H))
    g2d.set_color(b2.color())
    g2d.draw_rect(b2.pos(), (BALL_W, BALL_H))
    g2d.set_color(b3.color())
    g2d.draw_rect(b3.pos(), (BALL_W, BALL_H))

    b1.move()
    b2.move()
    b3.move()

def main():
    global b1, b2, b3
    b1 = Ball(150, 100)
    b2 = Ball(240, 80)
    b3 = Ball(300, 300)

    g2d.init_canvas((CANVAS_W, CANVAS_H))
    g2d.main_loop(tick)

if __name__ == "__main__":
    main()