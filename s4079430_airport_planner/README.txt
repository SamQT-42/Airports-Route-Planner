# Airports-Route-Planner
DEMO VIDEO: https://rmiteduau-my.sharepoint.com/:v:/g/personal/s4079430_rmit_edu_vn/IQACiN63GYKsRqHVfv-ovWTlAXicWWKdt9BbIJ8-FTo9fog?e=OlZ1wk
Mini Project from course COSC2469 - Algorithms and Analysis
## About

This program builds a route network from the *[OpenFlights dataset](https://github.com/jpatokal/openflights/tree/master/data)* and answers two questions for any pair of airports:

- What is the route with the **fewest flights**?
- What is the route with the **shortest total estimated distance** (calculated using the Haversine formula)?

Computed using **BFS(Breadth First Search)** for minimum stops, **Dijkstra's algorithm** for shortest distance

## Requirements

- Python 3 (developed and tested on Python 3.11 / 3.14)
- Standard Library only

## Setup

1. Clone this repository or download it as a ZIP.
2. Download `airports.dat` and `routes.dat` from the *[OpenFlights data folder](https://github.com/jpatokal/openflights/tree/master/data)* and place them inside `s4079430_airport_planner/data/`.

## How to run

Open a terminal inside the `s4079430_airport_planner` folder and run:

```bash
python main.py
```
You'll be shown a menu:
1. Calculate minimum stop route
2. Calculate shortest route
3. Calculate both
4. Exit the program

Pick an option, then enter a source and destination **IATA airport code** (for example `SGN` and `MEL`). After each result you can choose `1. BACK` to return to the menu or `2. FIND ANOTHER ROUTE` to keep querying in the same mode.

## Project structure
s4079430_airport_planner/

    ├── main.py entry point — menu, input, and orchestration
    ├── data_loader.py loads and cleans the OpenFlights data
    ├── algorithms.py BFS and Dijkstra implementations
    ├── README.txt
    └── data/
      ├── airports.dat
      └── routes.dat

## Key assumptions
- Airports with no valid IATA code are excluded, since queries are always by IATA code.
- Routes referencing an airport missing from the cleaned airport list are dropped before the network is built.
- Multiple airlines flying the same city pair count as a single connection.

## Author
Nguyễn Đặng Quốc An — s4079430 — COSC2469

## License
*[MIT](LICENSE)*

