import networkx as nx 
import matplotlib.pyplot as plt 

class Graph:
    class Vertex:
        def _init_(self, x):
            self._element = x

        def _str_(self):
            return str(self._element)

        def element(self):
            return self._element

        def _hash_(self):
            return hash(id(self))

    class Edge:
        def _init_(self, u, v, x):
            self._origin = u
            self._destination = v
            self._element = x

        def endpoints(self):
            return (self._origin, self._destination)

        def opposite(self, v):
            return self._destination if v is self._origin else self._origin

        def element(self):
            return self._element

        def _hash_(self):
            return hash((self._origin, self._destination))

    def _init_(self, directed=False):
        self._outgoing = {}
        self._incoming = {} if directed else self._outgoing

    def _str_(self):
        returning_value = '{'
        for vertex, edges in self._outgoing.items():
            returning_value += "'" + str(vertex) + "': ["
            for edge in edges:
                returning_value += "'" + str(edge) + "', "
            returning_value = returning_value[:-2] + '], '
        return returning_value[:-2] + '}'

    def is_directed(self):
        return self._incoming is not self._outgoing 

    def insert_vertex(self, x= None):
        v = self.Vertex(x)
        self._outgoing[v] = {}
        if self.is_directed():
            self._incoming[v] = {}
        return v

    def insert_edge(self, u, v, x=None):
        e = self.Edge(u, v, x)
        self._outgoing[u][v] = e
        self._incoming[v][u] = e

    def get_vertex(self, u):
        for vertex in self._incoming:
            if vertex.element() == u:
                return vertex

    def visualize(self):
        G = nx.Graph()
        elements = []
        for _, edges in self._incoming.items():
            for _, edge in edges.items():
                elements.append([edge.opposite(edge._origin).element(), edge.opposite(edge._destination).element()])
        G.add_edges_from(elements) 
        nx.draw_networkx(G) 
        plt.show() 

    def center(self):
        # Initialize center to be all vertices
        center = set(self._outgoing.keys())

        for vertex in self._outgoing:
            eccentricity = self.eccentricity(vertex)
            if eccentricity < len(center):
                center = set([vertex])
            elif eccentricity == len(center):
                center.add(vertex)

        return center

    def eccentricity(self, v):
        # Initialize distances to all other vertices as -1 (unreachable)
        distances = {vertex: -1 for vertex in self._outgoing.keys()}

        # Start from vertex v
        distances[v] = 0

        # Queue for BFS
        queue = [v]

        while queue:
            current_vertex = queue.pop(0)
            for neighbor in self._outgoing[current_vertex]:
                if distances[neighbor] == -1:
                    distances[neighbor] = distances[current_vertex] + 1
                    queue.append(neighbor)

        # Return the maximum distance
        return max(distances.values())

if __name__ == '__main__':
    # Define the graph
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'C', 'D'],
        'C': ['A', 'B', 'D'],
        'D': ['B', 'C', 'E', 'F'],
        'E': ['D', 'F'],
        'F': ['D', 'E']
    }
    
    graph_object = Graph()

    # Insert vertices
    for vertex in graph:
        graph_object.insert_vertex(vertex)

    # Insert edges
    for vertex, edges in graph.items():
        for edge in edges:
            v = graph_object.get_vertex(vertex)
            e = graph_object.get_vertex(edge)
            graph_object.insert_edge(v, e)

    # Visualize the graph
    print("Grafo:")
    graph_object.visualize()

    # Calculate and print the center of the graph
    center = graph_object.center()
    print("Centro del grafo:")
    print(center)