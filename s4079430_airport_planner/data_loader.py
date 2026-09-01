import csv
#mapping, skip airports with no IATA, and skip routes without airports
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

def load_routes(filepath, airports):
    graph = {code:set() for code in airports}
    with open(filepath, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if not row:
                continue
            source = row[2]
            destination = row[4]
            if source in airports and destination in airports:
                graph[source].add(destination)
    return graph

def load_network(airports_filepath, routes_filepath):
    airports = load_airports(airports_filepath)
    graph = load_routes(routes_filepath, airports)
    return airports, graph
