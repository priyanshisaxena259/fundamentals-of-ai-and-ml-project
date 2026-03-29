# Smart Route Finder using A* Algorithm

## Overview
This project uses the A-star (A*) search algorithm to find the shortest path between cities using heuristic based search.

---

## Features
- Uses A* algorithm
- Calculates g(n), h(n), f(n)
- Visualizes graph and shortest path

---

## Technologies Used
- Python 
- NetworkX
- Matplotlib

---

## Steps to run the project
1. Install dependencies:
   pip install -r requirements.txt

2. Run the program:
   python main.py

---

## Example
Available cities: ['Delhi', 'Bhopal', 'Jaipur', 'Indore', 'Nagpur', 'Mumbai']

Enter start city: Delhi

Enter destination city: Mumbai

Visiting: Delhi
g(n): 0, h(n): 15, f(n): 0

Visiting: Bhopal
g(n): 10, h(n): 10, f(n): 20

Visiting: Indore
g(n): 15, h(n): 5, f(n): 20

Visiting: Mumbai
g(n): 19, h(n): 0, f(n): 19

Shortest Path: Delhi → Bhopal → Indore → Mumbai

Total Cost: 19

---
