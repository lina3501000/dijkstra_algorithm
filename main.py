from heapq import heapify, heappop, heappush 
#https://www.datacamp.com/de/tutorial/dijkstra-algorithm-in-python?dc_referrer=https%3A%2F%2Fwww.google.com%2F$0
"""
heapify: Verwandelt eine Liste von Tupeln mit Priorität-Wert-Paaren in eine Prioritätswarteschlange.
heappush: Fügt der Warteschlange ein Element mit der entsprechenden Priorität hinzu.
heappop: Entfernt und gibt das Element mit der höchsten Priorität zurück (das Element mit dem kleinsten Wert)."""
graph = {
   "A": {"B": 3, "C": 3},
   "B": {"A": 3, "D": 3.5, "E": 2.8},
   "C": {"A": 3, "E": 2.8, "F": 3.5},
   "D": {"B": 3.5, "E": 3.1, "G": 10},
   "E": {"B": 2.8, "C": 2.8, "D": 3.1, "G": 7},
   "F": {"G": 2.5, "C": 3.5},
   "G": {"F": 2.5, "E": 7, "D": 10},
}
#print(graph["A"]["B"])
class Graph:
    def __init__(self, graph: dict={}): #macht dict
        self.graph=graph
    def add_edge(self, node1, node2, weight): #manuell knoten hinzufügen
        if node1 not in self.graph:
            self.graph[node1] ={}
        self.graph[node1][node2]=weight
    def shortest_distances(self, source: str):
        distance={node: float("inf") for node in self.graph} #alle anderen knoten werden auf unendlich gesetzt
        distance[source]=0 #entferung zu anfangspunkt wird auf null gesetzt
        #macht priority 
        pq=[(0, source)]
        heapify(pq)
        #macht set das besuchte knoten speichert
        visited=set()
        while pq: # an wenn priority queue ist nicht alle
            current_distance, current_node=heappop(pq) # gibt kleinste distance, und wird benannt
            if current_node in visited: #wenn min distance schon besucht, nimmt nächstes
                continue
            visited.add(current_node) #wenn nicht besucht wird in visited set hinzugefügt
            for neighbor, weight in self.graph[current_node].items():
                tentative_distance=current_distance+weight #tenterative:erwartbare,vorläufige, macht vorläufige distanz für jeden knoten drum herum
                if tentative_distance<distance[neighbor]:
                    distance[neighbor]=tentative_distance
                    heappush(pq,(tentative_distance, neighbor))
                """kp, was bei if abgeht: Für jeden Nachbarn berechnen wir die vorläufige Entfernung zum aktuellen Knoten, indem wir den aktuellen Wert des Nachbarn zum Gewicht 
                der Verbindungskante addieren. Dann prüfen wir, ob der Abstand kleiner ist als der Abstand des Nachbarn in distances. Wenn ja, aktualisieren 
                wir das distances Wörterbuch und fügen den Nachbarn mit seiner vorläufigen Entfernung in die Prioritätswarteschlange ein."""
        predecessors = {node: None for node in self.graph}


        for node, dist in distance.items():
            for neighbor, weight in self.graph[node].items():
                if distance[neighbor] == dist + weight:
                    predecessors[neighbor] = node

        return distance, predecessors
    def shortest_path(self, source: str, target: str):
        # Generate the predecessors dict
        _, predecessors = self.shortest_distances(source)

        path = []
        current_node = target

        # Backtrack from the target node using predecessors
        while current_node:
            path.append(current_node)
            current_node = predecessors[current_node]

        # Reverse the path and return it
        path.reverse()

        return path

G=Graph(graph)
start=input("Startknoten:")
if start not in G.graph:
   print("fehler, node gibt es nicht")
else: 
   distances, predecessors =G.shortest_distances(start)
print("distance:", distances)
print("node davor:", predecessors)
