
seasons = ("talvi", "talvi", "kevät","kevät","kevät", "kesä", "kesä", "kesä", "syksy", "syksy", "syksy", "talvi")
months = int(input("Anna kuukaden järjestysnumero (1-12): "))
month = seasons[months-1]
if months <= 12 and months > 0:
    print(f"{months}. kuukausi on {month}.")
else:
    print("Virhe")