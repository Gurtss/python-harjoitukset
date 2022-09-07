import random

def throw_dice(sides):
    dice = random.randint(1, sides)
    return dice

total_sides  = int(input("Anna nopan tahkojen määrä: "))


while True:
    dice_number = throw_dice(total_sides)
    print(dice_number)
    if dice_number == total_sides:
        break
