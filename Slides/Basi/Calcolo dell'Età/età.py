giorno_nascita = int(input("Inserire il giorno del mese di nascita: "))
mese_nascita = int(input("Inserire il mese dell'anno di nascita: "))
anno_nascita = int(input("Inserire l'anno di nascita: "))

giorno_attuale = int(input("Inserire il giorno attuale: "))
mese_attuale = int(input("Inserire il mese attuale: "))
anno_attuale = int(input("Inserire il anno attuale: "))

eta = anno_attuale - anno_nascita

if (mese_attuale < mese_nascita) or (mese_attuale == mese_nascita and giorno_attuale < giorno_nascita):
    eta -= 1

print(f"Hai {eta} anni.")