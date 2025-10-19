def create_words(alphabet: str) -> list[str]:
    """
    Crea tutte le possibili parole di tre lettere dato un certo insieme di lettere.
    :param alphabet: L'insieme di possibili lettere.
    :raises: ValueError Se l'alfabeto contiene lettere ripetute
    :return: La lista di tutte le possibili parole che si possono formare.
    """
    if len(alphabet) != len(set(alphabet)):
        raise ValueError("Impossibile avere caratteri uguali in un alfabeto.")

    words: list[str] = []

    for c1 in alphabet:
        for c2 in alphabet:
            for c3 in alphabet:
                words.append(f"{c1}{c2}{c3}")

    return words

def main():
    txt = input("Inserire un insieme di lettere: ")
    words = create_words(txt)

    print(f"Lista di tutte le parole ({len(words)}):")
    for w in words:
        print(w)

if __name__ == "__main__":
    main()