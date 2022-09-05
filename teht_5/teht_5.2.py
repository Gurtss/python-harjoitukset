# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon
# lopetusmerkiksi. Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen.
# Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi reverse=True.

numbers = []
readingNumbers = True
while readingNumbers:
    userInput = (input("Anna luku: "))
    if userInput == "":
        readingNumbers = False
    else:
        numbers.append(int(userInput))

numbers.sort(reverse=True)
print(numbers[:5])

for number in numbers[:5]:
    print(number)