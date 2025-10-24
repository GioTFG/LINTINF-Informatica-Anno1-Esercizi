from random import choice, randrange
from actor import Actor, Arena, Point

class Arthur(Actor):
    def __init__(self, pos):
        self._x, self._y = pos
        self._w, self._h = 20, 31
        self._speed = 2
        self._gravity = 2
        self._dy = 0
        self._state = "Idle"
        self._running_state = 1
        self._sprites = {
            "Idle": (6, 42),
            "RunningRight1": (40, 42),
            "RunningRight2": (66, 42),
            "RunningRight3": (88, 42),
            "RunningRight4": (109, 42),
            "RunningLeft1": (449, 43),
            "RunningLeft2": (427, 43),
            "RunningLeft3": (405, 43),
            "RunningLeft4": (379, 43)
        }

        self._sizes = {
            "Idle": (20, 32),
            "RunningRight1": (23, 32),
            "RunningRight2": (18, 32),
            "RunningRight3": (19, 32),
            "RunningRight4": (23, 32),
            "RunningLeft1": (23, 32),
            "RunningLeft2": (19, 32),
            "RunningLeft3": (18, 32),
            "RunningLeft4": (23, 32)
        }

    def move(self, arena: Arena):
        # Collisioni
        for other in arena.collisions():
            if isinstance(other, Ball):
                self.hit(arena)

        # Tasti
        keys = arena.current_keys()
        if "ArrowLeft" in keys:
            self._x -= self._speed
        if "ArrowRight" in keys:
            self._x += self._speed

        aw, ah = arena.size()

        # Gravità
        if "ArrowUp" in keys and self.is_on_ground():
            self._dy = -10

        if self._dy > 0:
            self._dy += self._gravity

        if self._y > ah - self._h:
            self._dy = 0
        else:
            self._dy += self._gravity
            self._y += self._dy

        # Controllo out of bounds
        self._x = min(max(self._x, 0), aw - self._w)
        self._y = min(max(self._y, 0), ah - self._h)

        self.set_state()

    def hit(self, arena: Arena):
        arena.kill(self)

    def pos(self) -> Point:
        return self._x, self._y

    def size(self) -> Point:
        if self._state in self._sizes:
            return self._sizes[self._state]
        return self._sizes["Idle"]

    def sprite(self) -> Point:
        # x, y = 6, 43
        # if "ArrowLeft" in keys:
        #     x, y = 450, 43
        # if "ArrowRight" in keys:
        #     x, y = 40, 43
        #
        # if "ArrowLeft" in keys and "ArrowRight" in keys:
        #     x, y = 6, 43

        if self._state in self._sprites:
            return self._sprites[self._state]
        else:
            return self._sprites["Idle"]

    def is_on_ground(self) -> bool:
        aw, ah = arena.size()
        return self._y >= ah - self._h

    def set_state(self):
        keys = g2d.current_keys()



        self._state = "Idle"

        if "ArrowLeft" in keys:
            self._state = "RunningLeft" + str(self._running_state + 1)
            self._running_state = ((self._running_state + 1) % 4)
        if "ArrowRight" in keys:
            self._state = "RunningRight" + str(self._running_state + 1)
            self._running_state = ((self._running_state + 1) % 4)

        if "ArrowLeft" in keys and "ArrowRight" in keys:
            self._state = "Idle"

def tick():
    g2d.clear_canvas()
    for a in arena.actors():
        if a.sprite() != None:
            g2d.draw_image("ghosts-goblins.png", a.pos(), a.sprite(), a.size())
        else:
            pass  # g2d.draw_rect(a.pos(), a.size())

    arena.tick(g2d.current_keys())  # Game logic


def main():
    global g2d, arena
    import g2d  # game classes do not depend on g2d

    arena = Arena((480, 360))
    # arena.spawn(Ball((40, 80)))
    # arena.spawn(Ball((80, 40)))
    # arena.spawn(Ghost((120, 80)))
    # arena.spawn(Turtle((230, 170)))

    player = Arthur((400, 0))
    arena.spawn(player)

    g2d.init_canvas(arena.size(), 2)
    g2d.main_loop(tick)

if __name__ == "__main__":
    main()
