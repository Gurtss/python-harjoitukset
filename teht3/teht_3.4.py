# Kirjoita ohjelma, joka kysyy vuosiluvun ja ilmoittaa, onko annettu vuosi karkausvuosi.
# Vuosi on karkausvuosi, jos se on jaollinen neljällä. Sadalla jaolliset vuodet ovat karkausvuosia vain
# jos ne ovat jaollisia myös neljälläsadalla.

vuosi = int(input("Anna vuosiluku: "))


def karkausvuosi(vuosi):
    if vuosi % 400 == 0:
        return True
    elif vuosi % 100 == 0:
        return False
    elif vuosi % 4 == 0:
        return True
    else:
        return False


if karkausvuosi(vuosi):
    print("Vuosi on karkausvuosi")
else:
    print("Vuosi ei ole karkausvuosi")

