anno = input("Inserire il proprio anno di nascita: ")

while not anno.isdigit():
    anno = input("Inserire il proprio anno di nascita: ")

anno = int(anno)
if anno % 12 == 2024 % 12:
    print("Il tuo anno è un anno del drago!")
else:
    print("Non sei nato in un anno del drago...")