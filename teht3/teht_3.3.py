sukupuoli = input("Kerro sukupuolesi(mies/nainen) ")
hemoglobiiniarvo = int(input("Kerro hemoglobiiniarvosi "))

if sukupuoli == "nainen":
    # testataan arvojen järkevyys"
    if not (5 < hemoglobiiniarvo < 300):
        print("virheellinen hemoglobiiniarvo!")
    elif hemoglobiiniarvo < 117:
        print("hemoglobiiniarvosi on alhainen")
    elif hemoglobiiniarvo <= 175:
        print("hemoglobiiniarvosi on normaali")
    else:
        print("hemoglobiiniarvosi on korkea")

elif sukupuoli == "mies":
    if not (5 < hemoglobiiniarvo < 300):
        print("virheellinen hemoglobiiniarvo!")
    elif hemoglobiiniarvo < 134:
        print("hemoglobiiniarvosi on alhainen")
    elif hemoglobiiniarvo <= 195:
        print("hemoglobiiniarvosi on normaali")
    else:
        print("hemoglobiiniarvosi on korkea")

else:
    pass