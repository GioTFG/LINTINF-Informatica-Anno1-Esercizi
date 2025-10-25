from random import choice, randrange
from actor import Actor, Arena, Point

class Arthur(Actor):
    def __init__(self, pos):
        self._x, self._y = pos
        self._w, self._h = 20, 31
        self._speed = 2
        self._gravity = 2
        self._dy = 0
        self._state = "IdleRight"
        self._running_state = 1

        self._direction = "Right"

        self._sprites = {
            "IdleRight": (134, 609),
            "IdleLeft": (358, 609),

            "RunningRight1": (5, 608),
            "RunningRight2": (39, 608),
            "RunningRight3": (72, 608),
            "RunningRight4": (102, 608),
            "RunningLeft1": (484, 608),
            "RunningLeft2": (454, 608),
            "RunningLeft3": (421, 608),
            "RunningLeft4": (386, 608),

            "JumpUpRight": (160, 613),
            "JumpDownRight": (194, 613),
            "JumpUpLeft": (320, 613),
            "JumpDownLeft": (291, 613),
        }

        self._sizes = {
            "IdleRight": (20, 31),
            "IdleLeft": (20, 31),
            "RunningRight1": (23, 32),
            "RunningRight2": (18, 32),
            "RunningRight3": (19, 32),
            "RunningRight4": (24, 32),
            "RunningLeft1": (23, 32),
            "RunningLeft2": (18, 32),
            "RunningLeft3": (19, 32),
            "RunningLeft4": (24, 32),

            "JumpUpRight": (32, 27),
            "JumpDownRight": (27, 27),
            "JumpUpLeft": (32, 27),
            "JumpDownLeft": (27, 27)
        }

    def move(self, arena: Arena):
        # Collisioni
        # for other in arena.collisions():
        #     if isinstance(other, Ball):
        #         self.hit(arena)

        self._dx = 0    # Serve per capire se c'è movimento negli sprite

        # Tasti
        keys = arena.current_keys()
        if "ArrowLeft" in keys:
            self._x -= self._speed
            self._direction = "Left"
        if "ArrowRight" in keys:
            self._x += self._speed
            self._direction = "Right"

        aw, ah = arena.size()

        # Gravità
        if "ArrowUp" in keys and self.is_on_ground():
            self._dy = -15

        if self._dy > 0:
            self._dy += self._gravity

        if self.is_on_ground() and not "ArrowUp" in keys:
            self._dy = 0
        else:
            self._dy += self._gravity
            self._y += self._dy

        # Controllo out of bounds
        self._x = min(max(self._x, 0), aw - self._w)
        self._y = min(max(self._y, 0), ah - self._h)

        self.set_state()
        # print(self._dy)

    def hit(self, arena: Arena):
        arena.kill(self)

    def pos(self) -> Point:
        return self._x, self._y

    def size(self) -> Point:
        if self._state in self._sizes:
            return self._sizes[self._state]
        return self._sizes["IdleRight"]

    def sprite(self) -> Point:
        if self._state in self._sprites:
            return self._sprites[self._state]
        else:
            return self._sprites["IdleRight"]

    def is_on_ground(self) -> bool:
        aw, ah = arena.size()
        return self._y >= ah - self._h

    def set_state(self):
        keys = g2d.current_keys()

        current_state = self._state
        self._state = "Idle" + self._direction

        if "ArrowLeft" in keys or "ArrowRight" in keys:
            self._state = "Running" + self._direction + str(self._running_state + 1)
            self._running_state = ((self._running_state + 1) % 4)

        if "ArrowLeft" in keys and "ArrowRight" in keys:
            self._state = "IdleRight"
            self._direction = "Right"

        if not self.is_on_ground():
            if self._dy > 0:
                self._state = "JumpDown" + self._direction
            elif self._dy < 0:
                self._state = "JumpUp" + self._direction


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
