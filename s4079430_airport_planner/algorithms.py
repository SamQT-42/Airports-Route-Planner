"""
@author
Student name: Nguyễn Đặng Quốc An
Student ID: s4079430
Course: COSC2469
"""

#BFS for tracking cheapest path (hops)
#Dijkstra for shortest distance (km)
#Haversine for determine the great-circle distance between two points on a sphere given their longitudes and latitudes.

import math
import heapq
from collections import deque

EARTH_RADIUS_KM = 6371.0

def haversine_km(lat1, lon1, lat2, lon2): #[1]
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    d_phi = math.radians(lat2 - lat1)
    d_lambda = math.radians(lon2 - lon1)
    
    a = (math.sin(d_phi/2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(d_lambda/2) ** 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    
    return EARTH_RADIUS_KM * c

def route_total_distance(route, airports):
    total = 0.0 
    for i in range(len(route) - 1):
        a = airports[route[i]]
        b = airports[route[i + 1]]
        total += haversine_km(a.latitude, a.longtitude, b.latitude, b.longtitude)
    return total

def _build_path(parent, source, destination):
    path = [destination]
    while path[-1] != source:
        path.append(parent[path[-1]])
    path.reverse()
    return path

def bfs_min_stops(graph, source, destination): #[2]
    if source == destination:
        return [source]
    visited = {source}
    parent = {}
    queue = deque([source])
    
    while queue:
        current = queue.popleft()
        for neighbour in sorted(graph[current]):
            if neighbour not in visited:
                visited.add(neighbour)
                parent[neighbour] = current
                if neighbour == destination:
                    return _build_path(parent, source, destination)
                queue.append(neighbour)
    return None

def dijkstra_shortest_distance(graph, airports, source, destination): #[3], [4]
    if source == destination:
        return [source], 0.0
    
    best_distance = {source: 0.0}
    parent = {}
    visited = set()
    priority_queue = [(0.0, source)]
    
    while priority_queue: #[6]
        current_distance, current = heapq.heappop(priority_queue)
        
        if current in visited:
            continue
        visited.add(current)
        
        if current == destination:
            break
        
        for neighbour in sorted(graph[current]):
            if neighbour in visited:
                continue
            
            edge_distance = haversine_km(
                airports[current].latitude, airports[current].longtitude,
                airports[neighbour].latitude, airports[neighbour].longtitude
            )
            new_distance = current_distance + edge_distance
            
            if neighbour not in best_distance or new_distance < best_distance[neighbour]:
                best_distance[neighbour] = new_distance
                parent[neighbour] = current
                heapq.heappush(priority_queue, (new_distance, neighbour))
                
    if destination not in best_distance:
        return None, None
    
    route = _build_path(parent, source, destination)
    return route, best_distance[destination]

"""
Reference list
[1] "Haversine formula," Wikipedia, The Free Encyclopedia. [Online]. Available: https://en.wikipedia.org/wiki/Haversine_formula. [Accessed: Sep. 1, 2026].
[2] "Breadth First Search or BFS for a Graph," GeeksforGeeks. [Online]. Available: https://www.geeksforgeeks.org/dsa/breadth-first-search-or-bfs-for-a-graph/. [Accessed: Sep. 1, 2026].
[3] "Dijkstra's algorithm," Wikipedia, The Free Encyclopedia. [Online]. Available: https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm. [Accessed: Sep. 1, 2026].
[4] "Implementing the Dijkstra Algorithm in Python: A Step-by-Step Tutorial," DataCamp, May 28, 2024. [Online]. Available: https://www.datacamp.com/tutorial/dijkstra-algorithm-in-python. [Accessed: Sep. 1, 2026].
[5] "Python Program For Dijkstra's Algorithm | Graph Data Structure," YouTube, Apr. 18, 2025. [Online]. Available: https://www.youtube.com/watch?v=u33NM1pZvoM. [Accessed: Sep. 1, 2026].
[6] "Performance improvement for Dijkstra algorithm using heaps in python?" Stack Overflow, Mar. 29, 2022. [Online]. Available: https://stackoverflow.com/questions/71663362/performance-improvement-for-dijkstra-algorithm-using-heaps-in-python. [Accessed: Sep. 1, 2026].
"""

    
                