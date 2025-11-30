"""
MERGE
- Definire una funzione merge
- Due parametri di tipo list
    - Entrambe le liste sono già ordinate (❗)
    - Entrambe le liste alla fine risulteranno vuote
- Risultato list
    - Risultato contiene tutti i valori delle due liste
    - I valori del risultato sono tutti in ordine
- Non usare sort, sorted; non ordinare la lista
    - Basta confrontare i valori in testa alle due liste
    - Quello più piccolo in assoluto è tra quei due
    - Rimuovere il valore scelto, dalla sua lista
"""

def merge(l1: list[int], l2: list[int]) -> list[int]:
    result = []
    while len(l1) > 0 and len(l2) > 0:
        if l1[0] < l2[0]:
            result.append(l1.pop(0))
        else:
            result.append(l2.pop(0))

    # Fill with remaining elements
    while len(l1) > 0:
        result.append(l1.pop(0))
    while len(l2) > 0:
        result.append(l2.pop(0))

    return result

list1 = [0, 2, 3, 5, 9, 10, 12]
list2 = [0, 3, 5, 6, 11, 13]

result = merge(list1, list2)

print(f"First list: {list1}")
print(f"Second list: {list2}")
print(f"Merged list: {result}")