import random

dices = int(input("Anna arpakuutioiden määrä: "))
total = 0

for dices in range(dices):
    throw = random.randint(1, 6)
    total += throw
    print(throw)

print(f"Silmälukujen summa on {total}")
