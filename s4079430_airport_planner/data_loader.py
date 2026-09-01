"""
@author
Student name: Nguyễn Đặng Quốc An
Student ID: s4079430
Course: COSC2469
link to Github repo: https://github.com/SamQT-42/Airports-Route-Planner
"""
import csv #[1], [2]
#mapping, skip airports with no IATA, and skip routes without airports(start and destination)
class Airports:
    def __init__(self, iata, name, country, latitude, longitude):
        self.iata = iata
        self.name = name
        self.country = country
        self.latitude = latitude
        self.longitude = longitude
        
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
            longitude = float(row[7])
            airports[iata] = Airports(iata, name, country, latitude, longitude)
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

"""
Reference List
[1] "Python CSV Module - Read and Write CSV Files," YouTube, 2022. [Online]. Available: https://www.youtube.com/watch?v=ozKsfsldV7M. [Accessed: Aug. 31, 2026].
[2] Indre, "Data cleaning in Python: A step-by-step guide," DataCamp, 2023. [Online]. Available: https://www.datacamp.com/tutorial/guide-to-data-cleaning-in-python. [Accessed: Aug. 31, 2026].
"""