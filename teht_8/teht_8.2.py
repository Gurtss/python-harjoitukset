import mysql.connector

# yhteyden avaus
yhteys = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database="flight_game",
    user="root",
    password="GioDio2209",
    autocommit=True
)

# määritetään kysely
maakoodi = input("Anna 2-kirjaiminen maakoodi: ")
sql = "SELECT TYPE ,COUNT(*) FROM airport where iso_country = '"+maakoodi+"' GROUP BY type"
print(sql)

kursori = yhteys.cursor()
kursori.execute(sql)

tulos = kursori.fetchall()
for rivi in tulos:
    print(f"{rivi[0]} {rivi[1]}")