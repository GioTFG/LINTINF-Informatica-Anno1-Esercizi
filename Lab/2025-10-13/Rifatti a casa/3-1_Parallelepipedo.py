class Parallelepipedo:
    def __init__(self, width, depth, height):
        self._width = width
        self._depth = depth
        self._height = height

    def volume(self) -> float:
        """
        Calcola il volume del parallelepipedo su cui viene chiamato il metodo.
        :return: Il volume del parallelepipedo.
        """
        return self._width * self._depth * self._height

    def diagonal(self) -> float:
        """
        Calcola la lunghezza della diagonale del parallelepipedo.
        :return: La lunghezza della diagonale.
        """
        return (self._width ** 2 + self._depth ** 2 + self._height ** 2) ** 0.5

def main():
    w, d, h = input("w, d, h del parallelepipedo: ").split()
    p = Parallelepipedo(float(w), float(d), float(h))
    print(f"Il parallelepipedo {w}x{d}x{h} ha volume {p.volume():.2f} e diagonale {p.diagonal():.2f}")

if __name__ == "__main__":
    main()