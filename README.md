Shortest Path Finder Application
Overview
This project is a Python-based desktop application that helps users find the shortest path between bus stops in a city based on criteria such as distance, time, or cost. The application leverages NetworkX for graph processing and Tkinter for the GUI, along with Matplotlib for visualizing the bus route on a map.

Features
User-Friendly Interface: The application provides a simple and intuitive GUI for selecting bus stops and criteria.
Shortest Path Calculation: Uses Dijkstra's algorithm to calculate the shortest path between two bus stops based on user-selected criteria (distance, time, or cost).
Graph Visualization: Displays the bus route on a map, highlighting the shortest path.
Dynamic Resizing: The map view supports scrolling and resizing for easier navigation.
Prerequisites
Ensure you have the following Python packages installed:

networkx
tkinter
matplotlib

You can install these dependencies using pip:

bash
Copy code
pip install networkx matplotlib
Note: tkinter is included with standard Python installations, so no separate installation is typically required.

How to Run

Copy code
python main.py
The application window will open. Select the starting and ending bus stops, choose the criteria (distance, time, or cost), and click "Find Shortest Path" to visualize the route.

Usage
Starting Bus Stop: Select the initial bus stop from the dropdown.
Ending Bus Stop: Select the destination bus stop.
Criteria: Choose whether you want to find the shortest path based on distance, time, or cost.
Find Shortest Path: Click this button to calculate and display the shortest path on the map.
File Structure
main.py: The main script that contains the application logic and GUI setup.
README.md: This file, which provides an overview and instructions for the project.
Contributions
Contributions are welcome! If you find any bugs or have suggestions for improvements, feel free to create an issue or submit a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details
