# Kirjoita while-toistorakennetta käyttävä ohjelma, joka tulostaa kolmella jaolliset luvut väliltä 1..1000.

i = 0

while i <= 1000:
    i += 1
    # tulostetaan kolmella jaolliset
    if i % 3 == 0:
        print(f"{i} on kolmella jaollinen")
