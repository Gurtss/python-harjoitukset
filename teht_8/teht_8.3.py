#8.3
import re
import mysql.connector
from geopy.distance import geodesic as distance


#yhteyden avaus
yhteys = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='root',
        password='GioDio2209',
        autocommit=True
        )

#funktio str muutokseen
def convert(name):
    new_name = ''.join(map(str, name))
    return new_name


#määritetään kysely
icao_1 = input("Anna ensimmäisen lentokentän ICAO-koodi: ")
icao_2 = input("Anna toisen lentokentän ICAO-koodi: ")
sql_name_1 = "SELECT name FROM airport WHERE ident = '" + icao_1 + "'"
sql_1 = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '" + icao_1 + "'"
sql_name_2 = "SELECT name FROM airport WHERE ident = '" + icao_2 + "'"
sql_2 = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '" + icao_2 + "'"

#suoritetaan kysely 1 NIMI
kursori = yhteys.cursor()
kursori.execute(sql_name_1)

#haetaan 1 NIMI
result_1_name = kursori.fetchall()
name_1 = convert(result_1_name)

#suoritetaan kysely 1 kordinaatit
kursori = yhteys.cursor()
kursori.execute(sql_1)
#haetaan 1 kordinaatit
result_1 = kursori.fetchall()


#suoritetaan kysely 2 NIMI
kursori = yhteys.cursor()
kursori.execute(sql_name_2)

#haetaan 2 NIMI
result_2_name = kursori.fetchall()
#muuntaa lentoaseman nimen str muotoon ja poistaa ylimääräiset merkit
name_2 = convert(result_2_name)

#suoritetaan kysely 2 kordinaatit
kursori = yhteys.cursor()
kursori.execute(sql_2)
#haetaan 2 kordinaatit
result_2 = kursori.fetchall()


#tulostaa vastauksen
print(name_1,"ja", name_2,"etäisyys on: ", round(distance(result_1, result_2).km, 2), " km")
