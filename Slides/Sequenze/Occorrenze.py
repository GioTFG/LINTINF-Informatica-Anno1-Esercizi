"""
OCCORRENZE
- Data una stringa contenente una sequenza di parole
    - Separate tra loro da uno spazio
- Contare le occorrenze di ogni parola della sequenza

Utilizzare un dizionario
"""

def count_occurrences(s: str):
    words = s.split(" ")
    word_occurrences = {}

    for word in words:
        if word in word_occurrences:
            word_occurrences[word] += 1
        else:
            word_occurrences[word] = 1

    return word_occurrences

txt = input("Inserire un testo: ")
print(count_occurrences(txt))