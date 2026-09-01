#BFS for tracking cheapest path (hops)
#Dijkstra for shortest distance (km)
#Haversine for determine the great-circle distance between two points on a sphere given their longitudes and latitudes.

import math
import heapq
from collections import deque

EARTH_RADIUS_KM = 6371.0

def haversine_km(lat1, lon1, lat2, lon2):
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

def bfs_min_stops(graph, source, destination):
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
                
                