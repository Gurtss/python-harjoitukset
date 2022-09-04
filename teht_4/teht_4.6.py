import numpy as np

N = int(input("Anna pisteiden määrä: "))
radius = 1
n = 0

xCoordinates = np.random.default_rng().uniform(-1, 1, (N,))
yCoordinates = np.random.default_rng().uniform(-1, 1, (N,))

for i in range(N):
    x = xCoordinates[i]
    y = yCoordinates[i]
    # Check if the points are inside the circle or not
    if x ** 2 + y ** 2 <= radius ** 2:
        n = n + 1

area = 4 * n / N
print("Pi:n arvo: ", area)
