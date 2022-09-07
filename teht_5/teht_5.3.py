# Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa, onko se alkuluku.
# Alkulukuja ovat luvut, jotka ovat jaollisia vain ykkösellä ja itsellään
# Esimerkiksi luku 13 on alkuluku, koska se voidaan jakaa vain luvuilla 1 ja 13 siten, että jako menee tasan.
# Toisaalta esimerkiksi luku 21 ei ole alkuluku, koska se voidaan jakaa tasan myös luvulla 3 tai luvulla 7.

whole_number = int(input("Anna kokonaisluku"))
numbers_list = [9, 8, 7, 6, 5, 4, 3, 2]
is_prime = False

if whole_number / whole_number == 1 and whole_number / 1 == whole_number:
    is_prime = True

for number in numbers_list:
   if whole_number % number == 0:
       is_prime = False


if is_prime == True:
    print(f"Luku {whole_number} on alkuluku")
else:
    print(f"Luku {whole_number} ei ole alkuluku")