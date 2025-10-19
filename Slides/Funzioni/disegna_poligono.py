import polar,g2d
from math import pi

def draw_poligon(n: int, center: tuple[float, float], radius: float) -> list[tuple[float, float]]:
    """
    Dato il centro, il raggio, disegna un poligono di n lati inscritto.
    :param n: Numero di lati del poligono
    :param center: Centro della circonferenza circoscritta
    :param radius: Raggio della circonferenza
    :return: Lista con coordinate dei vertici del poligono inscritto
    """
    angle = 360 / n
    vertices = []
    for i in range(n):
        a = angle * i
        x, y = polar.move_around(center, radius, a)
        vertices.append((x, y))

    return vertices

def main():
    g2d.init_canvas((500, 500))

    n = int(input("Inserire il numero di lati del poligono: "))
    x, y = input("Inserire coordinate del centro della circonferenza: ").split()
    c = (float(x), float(y))
    r = float(input("Inserire il raggio della circonferenza: "))
    vertices = draw_poligon(n, c, r)

    g2d.set_color((0, 0, 0))
    g2d.draw_circle(c, r)
    g2d.set_color((255, 255, 255))
    g2d.draw_circle(c, r - 5)

    g2d.set_color((255, 0, 0))
    for i in range(len(vertices)):
        g2d.draw_line(vertices[i - 1], vertices[i], 5)

    g2d.set_color((0, 0, 255))
    for v in vertices:
        g2d.draw_circle(v, 5)

    print(vertices)

    g2d.main_loop()

if __name__ == "__main__":
    main()