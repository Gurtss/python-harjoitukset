import random

def throw_dice():
    dice = random.randint(1, 6)
    return dice


while True:
    dice_number = throw_dice()
    print(dice_number)
    if dice_number == 6:
        break
