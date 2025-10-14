from random import choice, randrange

import g2d

CANVAS_W, CANVAS_H = 400, 400
BALL_W, BALL_H = 20, 20

class Ball:
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y
        self._dx = 2
        self._dy = 0

        self.change_color()

    def move(self):
        # if not 0 <= self._x + self._dx <= CANVAS_W - BALL_W:
        #     self._dx = -self._dx
        #     self.change_color()
        # if not 0 <= self._y + self._dy <= CANVAS_H - BALL_H:
        #     self._dy = -self._dy
        #     self.change_color()

        if self._x % 20 == 0 and self._y % 20 == 0:

            dirs = [(-2, 0), (2, 0), (0, -2), (0, 2)]
            dirs.remove((-self._dx, -self._dy))

            self._dx, self._dy = choice(dirs)

        self._x += self._dx
        self._y += self._dy

    def pos(self) -> tuple[int, int]:
        """
        :return: Restituisce la posizione (x, y) nel canvas della pallina.
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
    g2d.set_color(b.color())
    g2d.draw_image("ball.png", b.pos())

    b.move()

def main():
    global b
    b = Ball(200, 200)

    g2d.init_canvas((CANVAS_W, CANVAS_H))
    g2d.main_loop(tick)

if __name__ == "__main__":
    main()