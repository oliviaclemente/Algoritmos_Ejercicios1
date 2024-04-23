import networkx as nx 
import matplotlib.pyplot as plt 

class Graph:
# Representation of a simple graph using an adjacency map.

#------------------------- nested Vertex class -------------------------

    class Vertex:
    # Lightweight vertex structure for a graph.
        slots = '_element'

        def __init__(self, x):
        # Do not call constructor directly. Use Graph s insert_vertex(x).
            self._element = x

        def __str__(self) -> str:
            return self._element

        def element(self):
        # Return element associated with this vertex.
            return self._element
        
        def __len__(self):
            return len(self._element)

        def __hash__(self):
        # will allow vertex to be a map/set key
            return hash(id(self))

    #----------------------- nested Edge class -----------------------

    class Edge:
    # Lightweight edge structure for a graph.
        slots = '_origin' , '_destination' , '_element'

        def __init__(self, u, v, x):
        # Do not call constructor directly. Use Graph s insert_edge(u,v,x).
            self._origin = u
            self._destination = v
            self._element = x

        def endpoints(self):
        # Return (u,v) tuple for vertices u and v.
            return (self._origin, self._destination)

        def opposite(self, v):
        # Return the vertex that is opposite v on this edge.
            return self._destination if v is self._origin else self._origin

        def element(self):
        # Return element associated with this edge.
            return self._element

        def __hash__(self):
        # will allow edge to be a map/set key
            return hash((self._origin, self._destination))
    

    def __init__(self, directed=False):
    # Create an empty graph (undirected, by default).
    # Graph is directed if optional paramter is set to True.
        self._outgoing = { }
    # only create second map for directed graph; use alias for undirected
        self._incoming = { } if directed else self._outgoing

    def __str__(self):
        returning_value = '{'
        for vertex, edges in self._outgoing.items():
            returning_value += "'" + str(vertex) + "': ["
            for edge in edges:
                returning_value += "'" + str(edge) + "', "
            returning_value = returning_value[:-2] + '], '
        return returning_value[:-2] + '}'
    
    def is_directed(self):
    # Return True if this is a directed graph; False if undirected.
    # Property is based on the original declaration of the graph, 
    # not its contents.
        # directed if maps are distinct
        return self._incoming is not self._outgoing 

    def vertex_count(self):
    # Return the number of vertices in the graph.
        return len(self._outgoing)

    def vertices(self):
    # Return an iteration of all vertices of the graph.
        return self._outgoing.keys()

    def edge_count(self):
    # Return the number of edges in the graph.
        total = sum(len(self._outgoing[v]) for v in self._outgoing)
        # for undirected graphs, make sure not to double-count edges
        return total if self.is_directed( ) else total // 2

    def edges(self):
    # Return a set of all edges of the graph.
        # avoid double-reporting edges of undirected graph
        result = set( )
        for secondary_map in self._outgoing.values():
            # add edges to resulting set
            result.update(secondary_map.values())
        return result

    def get_vertex(self, u):
    # Return the vertex with the value u store.
    # If no vertex found return None.
        for vertex in self._incoming:
            if vertex._element == u:
                return vertex

    def get_edge(self, u, v):
    # Return the edge from u to v, or None if not adjacent.
    # returns None if v not adjacent
        return self._outgoing[u].get(v) 

    def degree(self, v, outgoing=True):
    # Return number of (outgoing) edges incident to vertex v in 
    # the graph.
    # If graph is directed, optional parameter used to count 
    # incoming edges.
        adj = self._outgoing if outgoing else self._incoming
        return len(adj[v])

    def incident_edges(self, v, outgoing=True):
    # Return all (outgoing) edges incident to vertex v in the graph.
    # If graph is directed, optional parameter used to request 
    # incoming edges.
        adj = self._outgoing if outgoing else self._incoming
        for edge in adj[v].values():
            yield edge

    def insert_vertex(self, x=None):
    # Insert and return a new Vertex with element x.
        v = self.Vertex(x)
        self._outgoing[v] = { }
        if self.is_directed():
            # need distinct map for incoming edges
            self._incoming[v] = { } 
        return v

    def insert_edge(self, u, v, x=None):
    # Insert and return a new Edge from u to v with 
    # auxiliary element x.
        e = self.Edge(u, v, x)
        self._outgoing[u][v] = e
        self._incoming[v][u] = e

    def visualize(self): 
        G = nx.Graph()
        elements = []
        for _, edges in self._incoming.items():
            for _, edge in edges.items():
                elements.append([edge._origin, edge._destination])
        G.add_edges_from(elements) 
        nx.draw_networkx(G) 
        plt.show() 

if __name__ == '__main__':
    # Simple implementation:
    # A -> B ; A -> C
    # B -> C ; B -> D
    # C -> D ; D -> C
    # E -> F ; F -> C
    graph = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']}
    
    graph_object = Graph()

    for vertice in graph:
        graph_object.insert_vertex(vertice)

    for vertice, edges in graph.items():
        for edge in edges:
            v = graph_object.get_vertex(vertice)
            e = graph_object.get_vertex(edge)
            graph_object.insert_edge(v, e)

    print(graph_object)
    print(graph)    
    graph_object.visualize()