graph = {
   "A": {"B": 3, "C": 3},
   "B": {"A": 3, "D": 3.5, "E": 2.8},
   "C": {"A": 3, "E": 2.8, "F": 3.5},
   "D": {"B": 3.5, "E": 3.1, "G": 10},
   "E": {"B": 2.8, "C": 2.8, "D": 3.1, "G": 7},
   "F": {"G": 2.5, "C": 3.5},
   "G": {"F": 2.5, "E": 7, "D": 10},
}



class Graph:
   def __init__(self, graph: dict = {}):
       self.graph = graph

   def add_edge(self, node1, node2, weight):
       if node1 not in self.graph:  # Check if the node is already added
           self.graph[node1] = {}  # If not, create the node
       self.graph[node1][node2] = weight  # Else, add a connection to its neighbor

   def shortest_distances(self, source: str):
       # Initialize the values of all nodes with infinity
       distances = {node: float("inf") for node in self.graph}
       distances[source] = 0  # Set the source value to 0

G=Graph()

G = Graph(graph)

#G.graph
# Sneak-peek - find the shortest paths from B
distances = G.shortest_distances("B")
print("distances:", distances)
to_F = distances["F"]
print(f"The shortest distance from B to F is {to_F}")
