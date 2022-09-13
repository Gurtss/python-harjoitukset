nimet = set()

while True:
    user_input = input("Anna nimi: ")
    if user_input in nimet:
        print("Annoit saman nimen.")
    elif user_input == "":
        break
    else:
        nimet.add(user_input)
        print("uusi nimi")

for n in nimet:
    print(n)