#1st iteration log(2PM 31/08/2026): Added simple entry point, and checks if data is cleaned before continue building
#2nd iteration log(): 
from data_loader import load_network

AIRPORTS_FILES = "data/airports.dat"
ROUTES_FILES = "data/routes.dat"

def main():
    airports, graph = load_network(AIRPORTS_FILES, ROUTES_FILES)
    total_edges = sum(len(neighbours) for neighbours in graph.values())
    print(f"Airports loaded: {len(airports)}")
    print(f"Routes kept after cleaning: {total_edges}")
    sample_code = "SGN"
    if sample_code in airports:
        sample = airports[sample_code]
        print(f"\nExample lookup - {sample_code}: {sample.name}, {sample.country} "f"({sample.latitude:.4f}, {sample.longtitude:.4f})")
        print(f"Destination from {sample_code}: {len(graph[sample_code])}")
        
if __name__ == "__main__":
    main()