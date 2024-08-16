import networkx as nx
from tkinter import *
from tkinter import ttk, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

graph = nx.Graph()

connections = [
    ('T Nagar', 'Vadapalani', {'distance': 3.0, 'time': 10, 'cost': 15}),
    ('Vadapalani', 'Ashok Nagar', {'distance': 2.0, 'time': 5, 'cost': 10}),
    ('Ashok Nagar', 'Koyambedu', {'distance': 4.0, 'time': 15, 'cost': 20}),
    ('Koyambedu', 'Arumbakkam', {'distance': 1.5, 'time': 5, 'cost': 10}),
    ('Arumbakkam', 'Thirumangalam', {'distance': 2.5, 'time': 10, 'cost': 15}),
    ('Thirumangalam', 'Anna Nagar', {'distance': 2.0, 'time': 7, 'cost': 10}),
    ('Anna Nagar', 'Egmore', {'distance': 6.0, 'time': 20, 'cost': 30}),
    ('Egmore', 'Central', {'distance': 2.0, 'time': 8, 'cost': 12}),
    ('Central', 'Parrys', {'distance': 3.0, 'time': 10, 'cost': 15}),
    ('Parrys', 'Mylapore', {'distance': 5.0, 'time': 15, 'cost': 20}),
    ('Mylapore', 'Adyar', {'distance': 4.0, 'time': 12, 'cost': 18}),
    ('Adyar', 'Thiruvanmiyur', {'distance': 2.5, 'time': 8, 'cost': 12}),
    ('Thiruvanmiyur', 'Velachery', {'distance': 6.0, 'time': 20, 'cost': 30}),
    ('Velachery', 'Tambaram', {'distance': 12.0, 'time': 30, 'cost': 40}),
    ('Tambaram', 'Chromepet', {'distance': 4.0, 'time': 12, 'cost': 15}),
    ('Chromepet', 'Guindy', {'distance': 8.0, 'time': 20, 'cost': 25}),
    ('Guindy', 'Saidapet', {'distance': 2.0, 'time': 7, 'cost': 10}),
    ('Saidapet', 'T Nagar', {'distance': 3.0, 'time': 10, 'cost': 15}),
    ('Velachery', 'Medavakkam', {'distance': 6.0, 'time': 20, 'cost': 25}),
    ('Medavakkam', 'Sholinganallur', {'distance': 8.0, 'time': 25, 'cost': 30}),
]

bus_stops = {start for start, end, data in connections}.union({end for start, end, data in connections})
graph.add_nodes_from(bus_stops)
graph.add_edges_from(connections)

positions = {
    'T Nagar': (4, 5),
    'Vadapalani': (3, 6),
    'Ashok Nagar': (2, 6),
    'Koyambedu': (1, 7),
    'Arumbakkam': (1, 8),
    'Thirumangalam': (1, 9),
    'Anna Nagar': (2, 10),
    'Egmore': (3, 11),
    'Central': (4, 11),
    'Parrys': (5, 12),
    'Mylapore': (5, 9),
    'Adyar': (6, 7),
    'Thiruvanmiyur': (7, 6),
    'Velachery': (7, 5),
    'Tambaram': (9, 4),
    'Chromepet': (8, 4),
    'Guindy': (6, 5),
    'Saidapet': (5, 6),
    'Medavakkam': (8, 3),
    'Sholinganallur': (9, 2),
}

def find_shortest_path(graph, start, end, weight):
    return nx.dijkstra_path(graph, start, end, weight=weight)

def on_submit():
    start_station = start_var.get()
    end_station = end_var.get()
    criteria = criteria_var.get().lower()

    try:
        shortest_path = find_shortest_path(graph, start_station, end_station, criteria)
        result_var.set(f"Shortest {criteria} Path: {shortest_path}")

        fig, ax = plt.subplots(figsize=(12, 8))

        node_colors = []
        for node in graph.nodes():
            if node in shortest_path:
                node_colors.append('orange')
            else:
                node_colors.append('lightgrey')

        nx.draw_networkx_nodes(graph, positions, node_color=node_colors, node_size=700, ax=ax)
        nx.draw_networkx_edges(graph, positions, edgelist=connections, edge_color='lightblue', width=2, ax=ax)
        path_edges = list(zip(shortest_path, shortest_path[1:]))
        nx.draw_networkx_edges(graph, positions, edgelist=path_edges, edge_color='red', width=4, ax=ax)

        nx.draw_networkx_labels(graph, positions, font_size=10, ax=ax)

        ax.annotate('Start', xy=positions[start_station], xytext=(-25, 25),
                    textcoords='offset points', arrowprops=dict(arrowstyle='->', color='black', lw=1.5),
                    bbox=dict(boxstyle="round,pad=0.3", edgecolor='black', facecolor='white'))

        ax.annotate('End', xy=positions[end_station], xytext=(-25, 25),
                    textcoords='offset points', arrowprops=dict(arrowstyle='->', color='black', lw=1.5),
                    bbox=dict(boxstyle="round,pad=0.3", edgecolor='black', facecolor='white'))

        for widget in plot_frame.winfo_children():
            widget.destroy()

        canvas = FigureCanvasTkAgg(fig, master=plot_frame)
        canvas.draw()
        
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(fill=BOTH, expand=True)

        x_scrollbar = Scrollbar(plot_frame, orient=HORIZONTAL, command=canvas_widget.xview)
        y_scrollbar = Scrollbar(plot_frame, orient=VERTICAL, command=canvas_widget.yview)
        
        canvas_widget.configure(xscrollcommand=x_scrollbar.set, yscrollcommand=y_scrollbar.set)

        x_scrollbar.pack(side=BOTTOM, fill=X)
        y_scrollbar.pack(side=RIGHT, fill=Y)
        
    except nx.NetworkXNoPath:
        messagebox.showerror("Error", "No path exists between the specified bus stops.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

root = Tk()
root.title("Shortest Path Finder")

root.state('zoomed')

start_var = StringVar()
end_var = StringVar()
criteria_var = StringVar()
result_var = StringVar()

all_stations = list(bus_stops)

padding = {'padx': 20, 'pady': 20}
font = ('Helvetica', 16)

Label(root, text="Starting Bus Stop:", font=font).grid(column=0, row=0, **padding)
start_menu = ttk.Combobox(root, textvariable=start_var, font=font, values=all_stations)
start_menu.grid(column=1, row=0, **padding)

Label(root, text="Ending Bus Stop:", font=font).grid(column=0, row=1, **padding)
end_menu = ttk.Combobox(root, textvariable=end_var, font=font, values=all_stations)
end_menu.grid(column=1, row=1, **padding)

Label(root, text="Criteria (distance/time/cost):", font=font).grid(column=0, row=2, **padding)
criteria_menu = ttk.Combobox(root, textvariable=criteria_var, font=font, values=['distance', 'time', 'cost'])
criteria_menu.grid(column=1, row=2, **padding)

submit_button = Button(root, text="Find Shortest Path", font=font, command=on_submit)
submit_button.grid(column=0, row=3, columnspan=2, **padding)

result_label = Label(root, textvariable=result_var, font=font)
result_label.grid(column=0, row=4, columnspan=2, **padding)

plot_frame = Frame(root)
plot_frame.grid(column=0, row=5, columnspan=2, sticky='nsew')

root.grid_rowconfigure(5, weight=1)
root.grid_columnconfigure(1, weight=1)

root.mainloop()
