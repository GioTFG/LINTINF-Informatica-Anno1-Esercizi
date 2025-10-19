def cels_to_fahr(cels: float) -> float:
    """
    Convertitore da Celsius a Fahrenheit
    :param cels: Temperatura in gradi Celsius
    :return: Temperatura in gradi Fahrenheit
    """
    return cels * 1.8 + 32

def main():
    c = float(input("Inserire la temperatura in Celsius: "))
    f = cels_to_fahr(c)
    print(f"{c:.2f}°C equivalgono a {f:.2f}°F.")

if __name__ == "__main__":
    main()