import networkx as nx
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

graph = nx.Graph()

blue_line_stations = [
    'washermanpet', 'mannadi', 'high court', 'central', 'government estate', 'lic',
    'thousand lights', 'ag-dms', 'teynampet', 'nandanam', 'saidapet', 'guindy',
    'little mount', 'airport'
]
graph.add_nodes_from(blue_line_stations)

blue_line_edges = [
    ('washermanpet', 'mannadi', {'distance': 1.5, 'time': 3, 'cost': 10}),
    ('mannadi', 'high court', {'distance': 1.0, 'time': 2, 'cost': 10}),
    ('high court', 'central', {'distance': 1.5, 'time': 3, 'cost': 10}),
    ('central', 'government estate', {'distance': 1.0, 'time': 2, 'cost': 10}),
    ('government estate', 'lic', {'distance': 1.2, 'time': 3, 'cost': 10}),
    ('lic', 'thousand lights', {'distance': 1.0, 'time': 2, 'cost': 10}),
    ('thousand lights', 'ag-dms', {'distance': 1.2, 'time': 3, 'cost': 10}),
    ('ag-dms', 'teynampet', {'distance': 1.3, 'time': 3, 'cost': 10}),
    ('teynampet', 'nandanam', {'distance': 1.5, 'time': 3, 'cost': 10}),
    ('nandanam', 'saidapet', {'distance': 1.8, 'time': 4, 'cost': 10}),
    ('saidapet', 'guindy', {'distance': 2.0, 'time': 5, 'cost': 10}),
    ('guindy', 'little mount', {'distance': 1.5, 'time': 3, 'cost': 10}),
    ('little mount', 'airport', {'distance': 6.5, 'time': 12, 'cost': 30}),
]
graph.add_edges_from(blue_line_edges)

green_line_stations = [
    'chennai central', 'egmore', 'ashok nagar', 'vadapalani', 'arumbakkam', 'koyambedu',
    'cmrl depot', 'thirumangalam', 'anna nagar tower', 'anna nagar east',
    'shenoy nagar', 'pachaiyappa\'s college'
]
graph.add_nodes_from(green_line_stations)

green_line_edges = [
    ('chennai central', 'egmore', {'distance': 1.5, 'time': 3, 'cost': 10}),
    ('egmore', 'ashok nagar', {'distance': 3.5, 'time': 6, 'cost': 20}),
    ('ashok nagar', 'vadapalani', {'distance': 1.5, 'time': 3, 'cost': 10}),
    ('vadapalani', 'arumbakkam', {'distance': 1.2, 'time': 3, 'cost': 10}),
    ('arumbakkam', 'koyambedu', {'distance': 1.5, 'time': 3, 'cost': 10}),
    ('koyambedu', 'cmrl depot', {'distance': 2.0, 'time': 4, 'cost': 10}),
    ('cmrl depot', 'thirumangalam', {'distance': 1.5, 'time': 3, 'cost': 10}),
    ('thirumangalam', 'anna nagar tower', {'distance': 1.2, 'time': 3, 'cost': 10}),
    ('anna nagar tower', 'anna nagar east', {'distance': 1.0, 'time': 2, 'cost': 10}),
    ('anna nagar east', 'shenoy nagar', {'distance': 1.2, 'time': 3, 'cost': 10}),
    ('shenoy nagar', 'pachaiyappa\'s college', {'distance': 1.5, 'time': 3, 'cost': 10}),
]
graph.add_edges_from(green_line_edges)

connections = [
    ('central', 'chennai central', {'distance': 0.5, 'time': 1, 'cost': 5}),
]
graph.add_edges_from(connections)

def find_shortest_path(graph, start, end, weight):
    return nx.dijkstra_path(graph, start, end, weight=weight)

def on_submit():
    start_station = start_var.get().lower()
    end_station = end_var.get().lower()
    criteria = criteria_var.get().lower()

    try:
        shortest_path = find_shortest_path(graph, start_station, end_station, criteria)
        result_var.set(f"Shortest {criteria} Path: {shortest_path}")

        pos = nx.spring_layout(graph, seed=42) 
        fig, ax = plt.subplots(figsize=(16, 9))

        node_colors = []
        for node in graph.nodes():
            if node in blue_line_stations and node in shortest_path:
                node_colors.append('deepskyblue')
            elif node in green_line_stations and node in shortest_path:
                node_colors.append('lightgreen')
            else:
                node_colors.append('lightgrey')

        nx.draw_networkx_nodes(graph, pos, node_color=node_colors, node_size=700, ax=ax)

        nx.draw_networkx_edges(graph, pos, edgelist=blue_line_edges, edge_color='deepskyblue', width=3, ax=ax, label='Blue Line')
        nx.draw_networkx_edges(graph, pos, edgelist=green_line_edges, edge_color='lightgreen', width=3, ax=ax, label='Green Line')

        path_edges = list(zip(shortest_path, shortest_path[1:]))
        nx.draw_networkx_edges(graph, pos, edgelist=path_edges, edge_color='red', width=4, ax=ax, label='Shortest Path')

        nx.draw_networkx_labels(graph, pos, font_size=10, ax=ax)

        ax.annotate('Start', xy=pos[start_station], xytext=(-25, 25),
                    textcoords='offset points', arrowprops=dict(arrowstyle='->', color='black', lw=1.5),
                    bbox=dict(boxstyle="round,pad=0.3", edgecolor='black', facecolor='white'))

        ax.annotate('End', xy=pos[end_station], xytext=(-25, 25),
                    textcoords='offset points', arrowprops=dict(arrowstyle='->', color='black', lw=1.5),
                    bbox=dict(boxstyle="round,pad=0.3", edgecolor='black', facecolor='white'))

        ax.legend(loc='upper right', fontsize=12)

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
        messagebox.showerror("Error", "No path exists between the specified stations.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

root = Tk()
root.title("Shortest Path Finder")

root.state('zoomed')

start_var = StringVar()
end_var = StringVar()
criteria_var = StringVar()
result_var = StringVar()

all_stations = blue_line_stations + green_line_stations

padding = {'padx': 20, 'pady': 20}
font = ('Helvetica', 16)

Label(root, text="Starting Station:", font=font).grid(column=0, row=0, **padding)
start_menu = ttk.Combobox(root, textvariable=start_var, font=font, values=all_stations)
start_menu.grid(column=1, row=0, **padding)

Label(root, text="Ending Station:", font=font).grid(column=0, row=1, **padding)
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
