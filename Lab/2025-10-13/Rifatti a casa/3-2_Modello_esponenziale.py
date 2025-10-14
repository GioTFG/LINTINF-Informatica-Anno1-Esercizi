from math import exp

class Exponential:
    def __init__(self, a: float, b: float, c: float):
        """
        Crea una funzione del tipo a * e^(bx) + c
        :param a: Coefficiente di e
        :param b: Esponente di e
        :param c: Termine noto
        """
        self._a = a
        self._b = b
        self._c = c

    def estimate(self, x: float) -> float:
        """
        Calcola il valore della funzione per x passata come parametro.
        :param x: Il valore da sostituire alla x nell'espressione
        :return: Il valore finale dell'espressione valutata.
        """
        return self._a * exp(self._b * x) + self._c

def main():
    a, b, c = input("Inserire i parametri della funzione (a, b, c): ").split()
    a = float(a)
    b = float(b)
    c = float(c)
    e = Exponential(a, b, c)

    x = input("Inserire il valore di x da sostituire (lasciare vuoto per terminare): ")
    while x != "":
        x = float(x)
        print(f"La funzione {a:.2f} * e^({x*b:.2f}) + {x:.2f} per {x: = } è {e.estimate(x):.2f}.")
        x = input("Inserire il valore di x da sostituire (lasciare vuoto per terminare): ")

if __name__ == "__main__":
    main()