import random

print("Numeri generati:")
num1 = random.randint(1, 6)
num2 = random.randint(1, 6)
num3 = random.randint(1, 6)

print(num1, num2, num3)

min = num1

for num in [num1, num2, num3]:
    if num < min:
        min = num

print(f"Il minimo è {min}.")