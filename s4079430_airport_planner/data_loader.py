#clean the data, drop contents that does not satisfy the format ID/Airport/FROM/TO/iata/longtitude/latitude

import csv
#mapping, skip airports with no IATA code
class Airports:
    def __init__(self, iata, name, country, latitude, longtitude):
        self.iata = iata
        self.name = name
        self.country = country
        self.latitude = latitude
        self.longtitude = longtitude
        
def load_airports(filepath):
    airports = {}
    with open(filepath, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if not row:
                continue
            
            iata = row[4]
            if iata == "\\N" or iata == "":
                continue
            name = row[1]
            country = row[3]
            latitude = float(row[6])
            longtitude = float(row[7])
            airports[iata] = Airports(iata, name, country, latitude, longtitude)
    return airports

