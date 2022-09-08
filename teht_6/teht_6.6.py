import math

def pizzan_arvo(halkaisija, hinta):
    sade = float(halkaisija / 2)
    pinta_ala_m = (math.pi * sade * sade) / 10000
    arvo = hinta / pinta_ala_m
    return arvo

def read_pizza_values(pizza_id):
    print(f"Anna {pizza_id+1}. pizzan tiedot")
    hinta = float(input("Syötä pizzan hinta (€): "))
    halkaisija = float(input("Syötä halkaisijan arvo (cm): "))
    pizzat.append(pizzan_arvo(halkaisija, hinta))


pizzat = []


lkm = int(input("Montako pizaa: "))
for x in range(lkm):
    read_pizza_values(x)

arvokkaimman_id = 0
for x in range(len(pizzat)):
    if pizzat[arvokkaimman_id] > pizzat[x]:
        arvokkaimman_id = x

print(f"Arvokkain pizza on {arvokkaimman_id +1}")