# Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10. Kone arvuuttelee lukua
# pelaajalta siihen asti, kunnes tämä arvaa oikein. Kunkin arvauksen jälkeen ohjelma tulostaa tekstin
# Liian suuri arvaus, Liian pieni arvaus tai Oikein. Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.

import random

random_number = random.randint(1, 10)

while True:
    user_input = int(input("Arvaa numero 1 ja 10 väliltä: "))
    if user_input == random_number:
        print("Oikein")
        break
    elif user_input < random_number:
        print("Liian pieni arvaus")
    else:
        print("Liian korkea arvaus")