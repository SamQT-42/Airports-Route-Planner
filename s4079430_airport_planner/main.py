"""
@author
Student name: Nguyễn Đặng Quốc An
Student ID: s4079430
Course: COSC2469
link to Github repo: https://github.com/SamQT-42/Airports-Route-Planner
"""

#1st iteration log: Added simple entry point, and checks if data is cleaned before continue building
#Test cases using sample data
#2nd iteration log: Apply BFS and testing (all test passed)
#3rd iteration log: Apply Dijskta and testing (all test passed)

import time
from algorithms import bfs_min_stops, route_total_distance, dijkstra_shortest_distance
from data_loader import load_network

AIRPORTS_FILES = "data/airports.dat"
ROUTES_FILES = "data/routes.dat"

def print_route(route, airports, distance=None):
    num_flights = len(route) - 1
    num_stops = max(num_flights - 1, 0)
    
    if distance is None:
        distance = route_total_distance(route, airports)
    print(f"Route: {' --> '.join(route)}")
    print(f"Number of flights: {num_flights}")
    print(f"Number of stops: {num_stops}")
    print(f"Total estimated distance: {distance:,.0f} km")

def main():
    airports, graph = load_network(AIRPORTS_FILES, ROUTES_FILES)
    source = input("Start from airport (IATA): ").upper()
    destination = input("Destination airport (IATA): ").upper()
    
    if source not in airports:
        print(f"\nError: {source} Source Code not found in dataset")
        return
    if destination not in airports:
        print(f"\nError: {destination} Destination Code not found in dataset")
        return
    
    print()
    
    start_time = time.perf_counter()
    min_stop_route = bfs_min_stops(graph, source, destination)
    min_stop_time = time.perf_counter() - start_time
    
    if min_stop_route is None:
        print(f"No route found from {source} to {destination}")
        return

    print("Minimum-stop route:")
    print_route(min_stop_route, airports)
    print(f"Running time: {min_stop_time:.4f} seconds")
    
    start_time = time.perf_counter()
    shortest_route, shortest_distance = dijkstra_shortest_distance(graph, airports, source, destination)
    shortest_time = time.perf_counter() - start_time
    
    print("\nShortest distance route:")
    print_route(shortest_route, airports, distance=shortest_distance)
    print(f"Running time: {shortest_time:.4f} seconds")
    
if __name__ == "__main__":
    main()