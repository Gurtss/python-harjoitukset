import random

def luo_pin():
    pinL = ""
    pinP = ""

    for i in range(3):
        pinL += str(random.randint(0, 9))
    for i in range(4):
        pinP += str(random.randint(1, 6))

    return pinL, pinP

if __name__ == "__main__":
    pinL, pinP = luo_pin()
    print(pinL)
    print(pinP)
