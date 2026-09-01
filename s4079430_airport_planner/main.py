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
#4th iteration log: Add UX and query loop
#5th iteration log: Major UX fixes: seperate options for minimum stop and shortest distance, added additional fallback messages after error.

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
    
def show_menu():
    print("\nWelcome to Airport Route Planner. What is on your mind?\n")
    print("1. Calculate minimum stop route")
    print("2. Calculate shortest route")
    print("3. Calculate both")
    print("4. Exit the program")
    
def get_route_query(airports):
    source = input("\nStart from airport (IATA): ").strip().upper()
    destination = input("\nDestination airport (IATA): ").strip().upper()
    
    if source not in airports:
        print(f"\nError: {source} Source code not found in dataset")
        return None
    if destination not in airports:
        print(f"\nError: {destination} Destination code not found in dataset")
        return None
    return source, destination

def ask_next_step():
    print("\n1. BACK")
    print("\n2. FIND ANOTHER ROUTE")
    nav = input("Choose an option: ").strip()
    return nav == "1"

def run_query(airports, graph, source, destination, mode):
    if mode in ("1", "3"):
        start_time = time.perf_counter()
        min_stop_route = bfs_min_stops(graph, source, destination)
        min_stop_time = time.perf_counter() - start_time

        if min_stop_route is None:
            print(f"\nNo route found from {source} to {destination}")
            return

    if mode in ("2", "3"):
        start_time = time.perf_counter()
        shortest_route, shortest_distance = dijkstra_shortest_distance(graph, airports, source, destination)
        shortest_time = time.perf_counter() - start_time

        if shortest_route is None:
            print(f"\nNo route found from {source} to {destination}")
            return

    if mode in ("1", "3"):
        print("\nMinimum-stop route:")
        print_route(min_stop_route, airports)
        print(f"Running time: {min_stop_time:.4f} seconds")

    if mode in ("2", "3"):
        print("\nShortest distance route:")
        print_route(shortest_route, airports, distance=shortest_distance)
        print(f"Running time: {shortest_time:.4f} seconds")
                
def main():
    airports, graph = load_network(AIRPORTS_FILES, ROUTES_FILES)
    while True:
        show_menu()
        choice = input("\nChoose an option:").strip()
        if choice == "4":
            print("\nThank you for using Airport Route Planner.")
            break
        if choice not in ("1", "2", "3"):
            print("\nPlease enter 1, 2, 3, or 4")
            continue
        
        while True:
            query = get_route_query(airports)
            if query is None:
                if ask_next_step():
                    break
                continue
            
            source, destination = query
            run_query(airports, graph, source, destination, choice)
            
            if ask_next_step():
                break
                
if __name__ == "__main__":
    main()