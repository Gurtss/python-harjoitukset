
def area(divider):
    import math
    a = math.pi * divider * divider
    return a
def unit_prize(area_a, prize):
    cost = area_a / prize
    return cost

prize_one = float(input("Anna pizzan 1 hinta: "))

divider_2 = float(input("Anna pizzan 1 halkaisia: "))

prize_two = float(input("Anna pizzan 2 hinta: "))

divider_two = float(input("Anna pizzan 2 halkaisia: "))

pizza_one_area = area(divider_2)

pizza_two_area = area(divider_two)

prize_one_area = unit_prize(pizza_one_area, prize_one)

prize_two_area = unit_prize(pizza_two_area, prize_two)

if prize_one_area > prize_two_area:
    print ("Pizza 1 on parempi vastine rahalle.")

else:
    print ("Pizza 2 on parempi vastine rahalle.")