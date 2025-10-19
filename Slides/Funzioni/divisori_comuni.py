def common_divisors(n1: int, n2: int) -> list[int]:
    """
    :param n1: Numero naturale
    :param n2: Numero naturale
    :return: Lista dei divisori comuni tra n1 e n2
    """
    divisors = []
    for n in range(1, min(n1, n2) + 1):
        if n1 % n == 0 and n2 % n == 0:
            divisors.append(n)

    return divisors

def main():
    n1, n2 = input("Inserire due numeri: ").split()
    n1, n2 = int(n1), int(n2)
    div = common_divisors(n1, n2)

    print("I divisori comuni sono:")
    for d in div:
        print(d)

if __name__ == "__main__":
    main()