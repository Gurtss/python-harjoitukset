# laske kaikkien kolmen grammat jaa 1000 niin saat kilogrammat sitten math.floor. Kilot = math.floor(grammaa/1000)
# leiviskä = 8320g
# naula = 416g
# luoti = 13,3g

import math

def kysymys():
    return float(input("Anna leiviskät: ")), float(input("Anna naulat: ")), float(input("Anna luodit: "))

def laske_naulat(leiviskät, naulat):
    return (leiviskät * 20) + naulat

def laske_luodit(naulat, luodit):
    return (naulat * 32) + luodit

def laske_grammat(luoti):
    return luoti * 13.3

def muunnakg(gramma):
    return gramma / 1000

if __name__ == "__main__":
    leiviskät, naulat, luodit = kysymys()
    kaikkinaulat = laske_naulat(leiviskät, naulat)
    kaikkiluodit = laske_luodit(kaikkinaulat, luodit)
    grammat = laske_grammat(kaikkiluodit)
    kilot = muunnakg(grammat)
    jämäg = grammat-math.floor(kilot)*1000

    print(f"{str(kilot).split('.')[0]} kg ja {round(jämäg, 2)} g")