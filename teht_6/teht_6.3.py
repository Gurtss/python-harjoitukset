def petrol(us_gallons):
    litre = us_gallons * 3.785411784
    return litre

give_gallons = int(input("Anna galloonien määrä: "))
total_litres = petrol(give_gallons)

while give_gallons >= 0:
    total_litres = petrol(give_gallons)
    print(f"{give_gallons} galloona on {total_litres} litraa")
    give_gallons = int(input("Anna galloonien määrä: "))
else:
    print("Käytä pos lukuja")



