# Kirjoita ohjelma, joka kysyy käyttäjältä viiden kaupungin nimet yksi kerrallaan
# (käytä for-toistorakennetta nimien kysymiseen) ja tallentaa ne listarakenteeseen.
# Lopuksi ohjelma tulostaa kaupunkien nimet yksi kerrallaan allekkain samassa järjestyksessä kuin ne syötettiin.
# Käytä for-toistorakennetta nimien kysymiseen ja for/in toistorakennetta niiden läpikäymiseen.


city = []
questions = 5

for question in range(questions):
    userInput = input("Anna kaupungin nimi: ")
    city.append(userInput)

for cities in city:
    print(cities)