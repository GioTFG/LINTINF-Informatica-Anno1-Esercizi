import g2d, polar

def draw_clock():
    g2d.set_color((0, 0, 0))

    angle = 360 / 12
    for i in range(12):
        pt1 = polar.move_around((250, 250), 100, angle * i + 90)
        pt2 = polar.move_around((250, 250), 150, angle * i + 90)

        g2d.draw_line(pt1, pt2, 5)

    angle = 360 / 60
    for i in range(60):
        pt1 = polar.move_around((250, 250), 130, angle * i + 90)
        pt2 = polar.move_around((250, 250), 150, angle * i + 90)

        g2d.draw_line(pt1, pt2, 5)

def main():
    g2d.init_canvas((500, 500))
    draw_clock()
    g2d.main_loop()

if __name__ == '__main__':
    main()