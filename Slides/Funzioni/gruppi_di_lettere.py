def count_groups(txt: str) -> tuple[int, int]:
    """
    Conta il numero di lettere nei gruppi [A-M] e [N-Z].
    :param txt: Testo di cui contare le lettere
    :return: Numero di lettere per i due gruppi
    """
    txt = txt.upper()

    am_letters: int = 0
    nz_letters: int = 0

    for c in txt:
        if "A" <= c <= "M":
            am_letters += 1
        if "N" <= c <= "Z":
            nz_letters += 1

    return am_letters, nz_letters

def main():
    txt = input("Inserire un testo: ")
    group1, group2 = count_groups(txt)
    print(f"Il testo ha {group1} lettere dalla 'A' alla 'M' e {group2} dalla 'N' alla 'Z'.")

if __name__ == "__main__":
    main()