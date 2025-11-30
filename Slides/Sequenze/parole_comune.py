"""
PAROLE COMUNI
- Date due stringhe s1 e s2 contenenti sequenze di parole
    - Separate tra loro da uno spazio
- Trovare l'insieme delle parole appartenenti a entrambe le stringhe
"""

def common_words(s1: str, s2: str) -> set[str]:
    common = set(s1.split(" ")) & set(s2.split(" "))
    return common

txt1 = input("Inserire un testo: ")
txt2 = input("Inserire un testo: ")
common = common_words(txt1, txt2)
print(common)