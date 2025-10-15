c_even = 0
c_odd = 0

txt: str = input("Inserire una stringa (lasciare vuoto per terminare): ")
while txt != "":
    for c in txt:
        if "a" <= c <= "z":
            if ord(c) % 2 == 0:
                c_even += 1
            else:
                c_odd += 1

    txt: str = input("Inserire una stringa (lasciare vuoto per terminare): ")

print(f"La parola {txt} ha {c_even} minuscole con unicode pari e {c_odd} dispari.")