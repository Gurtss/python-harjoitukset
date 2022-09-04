# Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan. Jos jompikumpi tai molemmat ovat väärin,
# tunnus ja salasana kysytään uudelleen. Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi
# kertaa. Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty. (Oikea käyttäjätunnus on python ja
# salasana rules).

username = "python"
password = "rules"
count = 1

while True:
    username = input("Anna käyttäjätunnus: ")
    password = input("Anna salasana: ")
    if username == "python" and password == "rules":
        print("Tervetuloa")
        break
    elif username != "python" or password != "rules":
        print(f"Väärin {5 - count} yritystä jäljellä")
        count += 1
    if count == 6:
        print("Pääsy evätty")
        break

