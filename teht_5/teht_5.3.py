# Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa, onko se alkuluku.
# Alkulukuja ovat luvut, jotka ovat jaollisia vain ykkösellä ja itsellään
# Esimerkiksi luku 13 on alkuluku, koska se voidaan jakaa vain luvuilla 1 ja 13 siten, että jako menee tasan.
# Toisaalta esimerkiksi luku 21 ei ole alkuluku, koska se voidaan jakaa tasan myös luvulla 3 tai luvulla 7.

number = int(input("Anna tasaluku: "))
divide = 2

while number > divide:
    if number % divide == 0:
        print("Ei ole alkuluku")
        break
    divide += 1
else:
    print(f"{number} on alkuluku")

