def perfect_square(num: int) -> tuple[bool, int]:
    """
    Dato un numero, dice se esso è un quadrato perfetto e, in tal caso, dice qual è la sua radice.
    :param num: Numero su cui cercare la radice
    :return: (True, int) se c'è il quadrato perfetto, (False, -1) se non lo è.
    """
    for n in range(0, num):
        if n * n == num:
            return True, n

    return False, -1

def main():
    n = int(input("Inserire un numero: "))
    ans = perfect_square(n)

    if ans[0]:
        print(f"{n} è un quadrato perfetto, la sua radice è: {ans[1]}.")
    else:
        print(f"{n} non è un quadrato perfetto.")

if __name__ == "__main__":
    main()