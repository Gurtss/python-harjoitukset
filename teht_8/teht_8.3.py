
import mysql.connector
from geopy import distance


#yhteyden avaus
yhteys = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='root',
        password='GioDio2209',
        autocommit=True
        )

def search(icao):
    sql = "select latitude_deg, longitude_deg from airport where gps_code = '"+icao+"'"
    cursor = yhteys.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    if cursor.rowcount > 0:
        return result
    else:
        print("Kenttää ei löydy")

locations = []
for i in range(2):
    icao = input(f"Anna {i+1}. ICAO koodi: ")
    locations.append(search(icao))
print(locations)

dist = distance.distance(locations[0], locations[1]).km
print(f"Etäisyys on {dist:.2f} km")