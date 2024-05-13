import osmnx as ox
import random
import heapq
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import networkx as nx

latitude = 25.4380
longuitude = -100.9737

G = ox.graph_from_point((latitude, longuitude), dist=10000, network_type="drive")

def style_unvisited_edge(edge):        
    G.edges[edge]["color"] = "#d36206"
    G.edges[edge]["alpha"] = 0.2
    G.edges[edge]["linewidth"] = 0.5

def style_visited_edge(edge):
    G.edges[edge]["color"] = "#d36206"
    G.edges[edge]["alpha"] = 1
    G.edges[edge]["linewidth"] = 1

def style_active_edge(edge):
    G.edges[edge]["color"] = '#e8a900'
    G.edges[edge]["alpha"] = 1
    G.edges[edge]["linewidth"] = 1

def style_path_edge(edge):
    G.edges[edge]["color"] = "white"
    G.edges[edge]["alpha"] = 1
    G.edges[edge]["linewidth"] = 1

def plot_graph():
    ox.plot_graph(
        G,
        node_size =  [ G.nodes[node]["size"] for node in G.nodes ],
        edge_color = [ G.edges[edge]["color"] for edge in G.edges ],
        edge_alpha = [ G.edges[edge]["alpha"] for edge in G.edges ],
        edge_linewidth = [ G.edges[edge]["linewidth"] for edge in G.edges ],
        node_color = "white",
        bgcolor = "#18080e"
    )

def dijkstra(orig, dest, plot=False):
    # Your graph initialization code
    for node in G.nodes:
        G.nodes[node]["visited"] = False
        G.nodes[node]["distance"] = float("inf")
        G.nodes[node]["previous"] = None
        G.nodes[node]["size"] = 0
    for edge in G.edges:
        style_unvisited_edge(edge)
    G.nodes[orig]["distance"] = 0
    G.nodes[orig]["size"] = 50
    G.nodes[dest]["size"] = 50
    pq = [(0, orig)]
    step = 0
    steps = []  # List to store graph states for each step

    while pq:
        _, node = heapq.heappop(pq)
        if node == dest:
            if plot:
                print("Iterations: ", step)
                # Capture the final state of the graph
                steps.append(nx.Graph(G))  # Copy the graph
            break  # Exit the loop once the destination is reached
        # Capture the current state of the graph
        steps.append(nx.Graph(G))  # Copy the graph

        if G.nodes[node]["visited"]:
            continue
        G.nodes[node]["visited"] = True

        for edge in G.out_edges(node):
            style_visited_edge((edge[0], edge[1], 0))
            neighbor = edge[1]
            weight = G.edges[(edge[0], edge[1], 0)]["weight"]
            if G.nodes[neighbor]["distance"] > G.nodes[node]["distance"] + weight:
                G.nodes[neighbor]["distance"] = G.nodes[node]["distance"] + weight
                G.nodes[neighbor]["previous"] = node
                heapq.heappush(pq, (G.nodes[neighbor]["distance"], neighbor))
                for edge2 in G.out_edges(neighbor):
                    style_active_edge((edge2[0], edge2[1], 0))
        step += 1

    if plot:
        # Plotting the animation
        fig, ax = plt.subplots()

        def update(frame):
            ax.clear()
            nx.draw(steps[frame], ax=ax)
            ax.set_title(f"Step {frame + 1}/{len(steps)}")

        ani = animation.FuncAnimation(fig, update, frames=len(steps), repeat=False)
        animation.save('ani.mp4', dpi=300) # to save animation

# Example usage:
# dijkstra(orig, dest, plot=True)

for edge in G.edges:
    maxspeed = 40
    if "maxspeed" in G.edges[edge]:
        maxspeed = G.edges[edge]["maxspeed"]
        if type(maxspeed) == list:
            speeds = [int(speed) for speed in maxspeed]
            maxspeed = min(speeds)
        elif type(maxspeed) == str:
            maxspeed = int(maxspeed)
        
    G.edges[edge]["maxspeed"] = maxspeed
    G.edges[edge]["weight"] = G.edges[edge]["length"] / maxspeed

start = random.choice(list(G.nodes))
end = random.choice(list(G.nodes))

dijkstra(start, end, plot=True)