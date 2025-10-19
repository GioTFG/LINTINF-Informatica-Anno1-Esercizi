def triangle_perimeter(a: float, b: float, c: float) -> float:
    """
    Controlla se i lati formano effettivamente un triangolo.
    Calcola il perimetro del triangolo dati i lati.
    :param a: Lato di un triangolo
    :param b: Lato di un triangolo
    :param c: Lato di un triangolo
    :raises: ValueError se i lati non formano un triangolo
    :return: Perimetro del triangolo
    """
    if a > b + c or b > a + c or c > a + b:
        raise ValueError("I lati non formano un triangolo")
    return a + b + c

def main():
    ans = "Y"
    while ans == "Y":
        a, b, c = input("Inserire i tre lati di un triangolo: ").split()
        a, b, c = float(a), float(b), float(c)
        peri = triangle_perimeter(a, b, c)
        print(f"Il perimetro del triangolo è {peri:.2f}.")

        ans = input("Vuoi continuare (Y/N): ").upper()

if __name__ == "__main__":
    main()