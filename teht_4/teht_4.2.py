# Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan kunnes
# käyttäjä antaa negatiivisen tuumamäärän. Sen jälkeen ohjelma lopettaa toimintansa.
# 1 tuuma = 2.54 centimeters

tuumat = int(input("Anna tuumien määrä: "))

while tuumat >= 0:
    cm = 2.54 * tuumat
    print(f"{tuumat} tuumaa on = {cm}cm")
    tuumat = int(input("Anna tuumien määrä: "))
print("Virheellinen luku, käytä vain positiivisia lukuja")



