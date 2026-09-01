Airport Route Planner
COSC2469 - Algorithms & Analysis - Mini Project
Student: Nguyen Dang Quoc An (s4079430)


1. ENVIRONMENT SETUP
---------------------
Requires Python 3 (developed and tested with Python 3.11 / 3.14). No
external libraries are required - only the Python Standard Library
(csv, math, time, heapq, collections).

Steps:
1. Install Python 3 from https://www.python.org/downloads/ if not already
   installed (on Windows, tick "Add Python to PATH" during install).
2. Make sure the project folder has this structure:

     s4079430_airport_planner/
       main.py
       data_loader.py
       algorithms.py
       data/
         airports.dat
         routes.dat

   airports.dat and routes.dat are the OpenFlights dataset files from:
   https://github.com/jpatokal/openflights/tree/master/data


2. HOW TO RUN
---------------------
1. Open a terminal (Command Prompt / PowerShell / Terminal).
2. Change directory into the s4079430_airport_planner folder, e.g.:
       cd path\to\s4079430_airport_planner
3. Run:
       python main.py
   (use "python3 main.py" if "python" is not recognised)
4. Enter a source airport IATA code when prompted, then a destination
   IATA code (e.g. SGN, then MEL).
5. The program prints the minimum-stop route and the shortest-distance
   route, each with the flight sequence, number of flights, number of
   stops, total estimated distance, and running time.

Each run answers one query. To try another source/destination pair,
run "python main.py" again.


3. ASSUMPTIONS MADE
---------------------
- Airports with no usable IATA code in airports.dat (stored as "\N" or
  blank in the raw data) are excluded, since the program only looks
  airports up by IATA code and such an airport could never be entered
  as a valid query anyway.
- Any route in routes.dat whose source or destination airport is not
  present in the cleaned airport list above is dropped before the
  route network is built. This follows the unit's own guidance that,
  since this assessment is about algorithmic thinking rather than
  error handling, missing/inconsistent data may be cleaned before use.
  (See the Data Structure section of the technical report for the
  exact number of routes this removed.)
- When multiple airlines fly the same direct source-destination pair,
  this is treated as a single directed connection in the route
  network, since the planner reasons about reachability and distance
  between airports, not about which airline operates the flight.
- Airport IATA codes are accepted case-insensitively (converted to
  uppercase automatically).


4. DEMO VIDEO
---------------------
OneDrive link (accessible to the teaching team): [ADD LINK HERE AFTER
RECORDING AND UPLOADING THE DEMO VIDEO]
