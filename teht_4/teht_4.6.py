import random

N = int(input("Anna pisteiden määrä: "))
n = 0
i = 0

while i <= N:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x ** 2 + y ** 2 <= 1:
        n = n + 1
    i = i + 1

area = 4 * n / N
print("Pi:n arvo: ", area)


