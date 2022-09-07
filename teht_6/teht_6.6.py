import math

def pizza_count(divider, prize):
    radius = divider / 2
    area = math.pi * radius ** 2
    print(area)

pizzarange = 2

for pizza in range(pizzarange):
    circle_divider = int(input("Anna halkaisijan arvo: "))
    pizza_prize = int(input("Anna pizzan hinta: "))
    pizza_count(circle_divider, pizza_prize)