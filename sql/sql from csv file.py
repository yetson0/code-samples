import sqlite3
import csv
import os

conn=sqlite3.connect(':memory:') # -> 'data.db'
cur=conn.cursor()

cur.execute("DROP TABLE IF EXISTS flights")
cur.execute('''
CREATE TABLE "flights" (
    id INTEGER NOT NULL PRIMARY KEY,
    tailNumber TEXT(6), 
    sourceAirportCode TEXT(3),
    destinationAirportCode TEXT(3),
    sourceCountryCode TEXT(3),
    destinationCountryCode TEXT(3),
    departureTimeUtc DATETIME,
    landingTimeUtc DATETIME
)
''')
# csv structure:
# tailNumber;
# source_airport_code;
# source_country_code;
# destination_airport_code;
# destination_country_code;
# departure_time;
# landing_time


fname="flightlegs.csv"
# fname="https://bitpeak.pl/datasets/flightlegs.csv"


with open(fname) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=";")
    for row in csv_reader:
        # print (row) # row check
        tail=row[0]
        srcapt=row[1]
        destapt=row[2]
        srcco=row[3]
        destco=row[4]
        dept=row[5]
        arri=row[6]
        cur.execute('''INSERT INTO flights(tailNumber,sourceAirportCode,destinationAirportCode,sourceCountryCode,destinationCountryCode,departureTimeUtc,landingTimeUtc) VALUES (?,?,?,?,?,?,?)''',(tail,srcapt,srcco,destapt,destco,dept,arri))
        # print (cur.fetchall())
        conn.commit()


# sql = """
# SELECT * FROM data
# """

cur.execute("SELECT * FROM flights")
print(cur.fetchall())


# # def runquery(phrase):
# # with conn:
#   # conn.execute(phrase)



# # runquery(phrase)
