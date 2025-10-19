from math import pi

def ellipse_area(a: float, b:float) -> float:
    """
    Calcola l'area di una data ellisse
    :param a: Primo semiasse dell'ellisse
    :param b: Secondo semiasse dell'ellisse
    :return: Area dell'ellisse
    """
    return pi * a * b

def main():
    a, b = input("Inserire le lunghezze dei due semiasse dell'ellisse: ").split()
    a = float(a)
    b = float(b)
    area = ellipse_area(a, b)
    print(f"L'area dell'ellisse è: {area:.2f}")

if __name__ == "__main__":
    main()