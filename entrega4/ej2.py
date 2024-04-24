import networkx as nx 
import matplotlib.pyplot as plt 

class Graph:
    class Vertex:
        def __init__(self, x):
            self._element = x

        def __str__(self):
            return str(self._element)

        def element(self):
            return self._element

        def __hash__(self):
            return hash(id(self))

    class Edge:
        def __init__(self, u, v, x):
            self._origin = u
            self._destination = v
            self._element = x

        def endpoints(self):
            return (self._origin, self._destination)

        def opposite(self, v):
            return self._destination if v is self._origin else self._origin

        def element(self):
            return self._element

        def __hash__(self):
            return hash((self._origin, self._destination))

    def __init__(self, directed=False):
        self._outgoing = {}
        self._incoming = {} if directed else self._outgoing

    def __str__(self):
        returning_value = '{'
        for vertex, edges in self._outgoing.items():
            returning_value += "'" + str(vertex) + "': ["
            for edge in edges.values():
                returning_value += "'" + str(edge) + "', "
            returning_value = returning_value[:-2] + '], '
        return returning_value[:-2] + '}'

    def is_directed(self):
        return self._incoming is not self._outgoing 

    def insert_vertex(self, x=None):
        v = self.Vertex(x)
        self._outgoing[v] = {}
        if self.is_directed():
            self._incoming[v] = {}
        return v

    def insert_edge(self, u, v, x=None):
        e = self.Edge(u, v, x)
        self._outgoing[u][v] = e
        self._incoming[v][u] = e

    def visualize(self):
        G = nx.Graph()
        elements = []
        for _, edges in self._outgoing.items():
            for edge in edges.values():
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

# Función para generar un grafo aleatorio
def generate_random_graph(n, p):
    G = nx.gnp_random_graph(n, p)
    return G

# Función para convertir un grafo de networkx a nuestra implementación de Graph
def convert_to_graph(G):
    graph = Graph()
    vertex_map = {}  # Mapeo de nodos de NetworkX a nodos de Graph

    for node in G.nodes():
        v = graph.insert_vertex(node)
        vertex_map[node] = v

    for edge in G.edges():
        u = vertex_map[edge[0]]
        v = vertex_map[edge[1]]
        graph.insert_edge(u, v)

    return graph

def is_center_unique(center):
    return len(center) == 1

# Generar tres configuraciones de red diferentes y calcular sus centros
def generate_and_check_networks():
    for i in range(3):
        print(f"Red {i+1}:")
        G = generate_random_graph(10, 0.3)  # Red aleatoria de 10 nodos con probabilidad de conexión 0.3
        graph = convert_to_graph(G)
        graph.visualize()
        center = graph.center()
        print("Centro del grafo:")
        print(center)
        if is_center_unique(center):
            print("El centro del grafo es único.")
        else:
            print(f"El grafo tiene {len(center)} centros distintos.")

if __name__ == '__main__':
    generate_and_check_networks()

