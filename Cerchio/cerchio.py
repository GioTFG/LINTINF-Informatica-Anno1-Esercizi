import g2d, re, math

dimensioni_canvas = (500, 500)
g2d.init_canvas(dimensioni_canvas)

raggio = g2d.prompt("Inserire il raggio del cerchio [0-200]: ")

if re.match(r"^-?\d+(\.\d+)?$", raggio) is None:
    g2d.alert("Il raggio inserito non è un numero.")
else:
    raggio = float(raggio)

    if 0 <= raggio <= 200:
        g2d.set_color((255, 117, 24))
        g2d.draw_circle((250, 250), raggio)

        g2d.set_color((0, 0, 0))
        g2d.draw_text(f"Area: {math.pi * (raggio ** 2):.2f}", (250, 225 - raggio), 25)
        g2d.draw_text(f"Circonferenza: {2 * math.pi * raggio:.2f}", (250, 275 + raggio), 25)
    else:
        g2d.alert("Il raggio inserito non è nel range [0-200]!")

g2d.main_loop()