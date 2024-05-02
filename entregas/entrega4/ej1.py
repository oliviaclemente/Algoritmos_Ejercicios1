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
            for edge in edges:
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
        center = set(self._outgoing.keys())

        for vertex in self._outgoing:
            eccentricity = self.eccentricity(vertex)
            if eccentricity < len(center):
                center = set([vertex])
            elif eccentricity == len(center):
                center.add(vertex)

        return center

    def eccentricity(self, v):
        distances = {vertex: -1 for vertex in self._outgoing.keys()}

    
        distances[v] = 0

        
        queue = [v]

        while queue:
            current_vertex = queue.pop(0)
            for neighbor in self._outgoing[current_vertex]:
                if distances[neighbor] == -1:
                    distances[neighbor] = distances[current_vertex] + 1
                    queue.append(neighbor)

        return max(distances.values())


def generate_random_graph(n, p):
    G = nx.gnp_random_graph(n, p)
    return G


def convert_to_graph(G):
    graph = Graph()
    vertex_map = {} 

    for node in G.nodes():
        v = graph.insert_vertex(node)
        vertex_map[node] = v

    for edge in G.edges():
        u = vertex_map[edge[0]]
        v = vertex_map[edge[1]]
        graph.insert_edge(u, v)

    return graph


if __name__ == '__main__':
   
    graph_object = Graph()

    central_node = graph_object.insert_vertex("Central")

    outer_nodes = ["Node_" + str(i) for i in range(1, 6)]
    for node in outer_nodes:
        new_node = graph_object.insert_vertex(node)
        graph_object.insert_edge(central_node, new_node)

    center = graph_object.center()
    if len(center) == 1:
        print("El centro del grafo es único.")
    else:
        print("El centro del grafo no es único.")

    print("Grafo Estrellado:")
    graph_object.visualize()

    # Configuración 1: Grafo completo de 5 nodos
    complete_graph = Graph()
    nodes = [complete_graph.insert_vertex("Node_" + str(i)) for i in range(1, 6)]
    for i in range(5):
        for j in range(i+1, 5):
            complete_graph.insert_edge(nodes[i], nodes[j])
    print("Centro del grafo completo de 5 nodos:", complete_graph.center())

    # Configuración 2: Grafo lineal de 5 nodos
    line_graph = Graph()
    nodes = [line_graph.insert_vertex("Node_" + str(i)) for i in range(1, 6)]
    for i in range(4):
        line_graph.insert_edge(nodes[i], nodes[i+1])
    print("Centro del grafo lineal de 5 nodos:", line_graph.center())

    # Configuración 3: Grafo de estrella invertida de 5 nodos
    inverted_star_graph = Graph()
    central_node = inverted_star_graph.insert_vertex("Central")
    outer_nodes = [inverted_star_graph.insert_vertex("Node_" + str(i)) for i in range(1, 6)]
    for node in outer_nodes:
        inverted_star_graph.insert_edge(node, central_node)
    print("Centro del grafo de estrella invertida de 5 nodos:", inverted_star_graph.center())
