import networkx as nx
import matplotlib.pyplot as plt

class Grafo:
    # Clase anidada para representar vértices
    class Vertice:
        def __init__(self, x):
            self._elemento = x

        def __str__(self):
            return str(self._elemento)

        def elemento(self):
            return self._elemento

        def __hash__(self):
            return hash(id(self))

    # Clase anidada para representar aristas
    class Arista:
        def __init__(self, u, v, x):
            self._origen = u
            self._destino = v
            self._elemento = x

        def extremos(self):
            return (self._origen, self._destino)

        def opuesto(self, v):
            return self._destino if v is self._origen else self._origen

        def elemento(self):
            return self._elemento

        def __hash__(self):
            return hash((self._origen, self._destino))

    def __init__(self, dirigido=False):
        self._saliente = {}  # Diccionario para almacenar las aristas salientes de cada vértice
        self._entrante = {} if dirigido else self._saliente  # Por si el grafo es no dirigido

    def __str__(self):
        valor_retorno = '{'
        for vertice, aristas in self._saliente.items():
            valor_retorno += "'" + str(vertice) + "': ["
            for arista in aristas:
                valor_retorno += "'" + str(arista) + "', "
            valor_retorno = valor_retorno[:-2] + '], '
        return valor_retorno[:-2] + '}'  # Retornar una representación de cadena del grafo

    def es_dirigido(self):
        return self._entrante is not self._saliente  # Ver si el grafo es dirigido

    def insertar_vertice(self, x=None):
        v = self.Vertice(x)  # nuevo vértice con el elemento dado
        self._saliente[v] = {}  # diccionario vacío 
        if self.es_dirigido():
            self._entrante[v] = {}  #dicc vacío (grafo dirigirdo) 
        return v

    def insertar_arista(self, u, v, x=None):
        e = self.Arista(u, v, x)  #nueva arista
        self._saliente[u][v] = e  # Agregar la arista al diccionario
        self._entrante[v][u] = e  #(grafo es dirigido) agregar la arista al diccionario 

    def obtener_vertice(self, u):
        for vertice in self._entrante:
            if vertice.elemento() == u:
                return vertice  #vértice por su elemento

    def visualizar(self):
        G = nx.Graph()  # nuevo grafo de NetworkX
        elementos = []
        for _, aristas in self._entrante.items():
            for _, arista in aristas.items():
                elementos.append([arista.opuesto(arista._origen).elemento(), arista.opuesto(arista._destino).elemento()])
        G.add_edges_from(elementos)  # Agregar las aristas al grafo 
        nx.draw_networkx(G)  #dibujar grafo
        plt.show() 

    def centro(self):
        centro = set(self._saliente.keys())  

        for vertice in self._saliente:
            excentricidad = self.excentricidad(vertice)  # excentricidad del vértice
            if excentricidad < len(centro):
                centro = set([vertice])  # Si la excentricidad es menor, actualizar el conjunto de vértices del centro
            elif excentricidad == len(centro):
                centro.add(vertice)  # Si la excentricidad es igual, agregar el vértice al conjunto de vértices del centro

        return centro  
    def excentricidad(self, v):
        distancias = {vertice: -1 for vertice in self._saliente.keys()}  # diccionario de distancias con valores -1

        distancias[v] = 0  # distancia del vértice a sí mismo es 0

        cola = [v]  # una cola 

        while cola:
            vertice_actual = cola.pop(0)  #primer vértice
            for vecino in self._saliente[vertice_actual]:  # Recorrer
                if distancias[vecino] == -1:
                    distancias[vecino] = distancias[vertice_actual] + 1  # Actualizar la distancia
                    cola.append(vecino) 

        return max(distancias.values())  


def generar_grafo_aleatorio(n, p):
    G = nx.gnp_random_graph(n, p) 
    return G


def convertir_a_grafo(G):
    grafo = Grafo()  #objeto de tipo Grafo
    mapeo_vertices = {}  

    for nodo in G.nodes():
        v = grafo.insertar_vertice(nodo)  # vértice en el Grafo 
        mapeo_vertices[nodo] = v  

    for arista in G.edges():
        u = mapeo_vertices[arista[0]]  # Obtener el vértice origen de la arista
        v = mapeo_vertices[arista[1]]  # Obtener el vértice destino de la arista
        grafo.insertar_arista(u, v)  # Insertar una arista 

    return grafo


if __name__ == '__main__':
    objeto_grafo = Grafo()

    nodo_central = objeto_grafo.insertar_vertice("Central")

    nodos_externos = ["Nodo_" + str(i) for i in range(1, 6)]
    for nodo in nodos_externos:
        nuevo_nodo = objeto_grafo.insertar_vertice(nodo)
        objeto_grafo.insertar_arista(nodo_central, nuevo_nodo)

    centro = objeto_grafo.centro()
    if len(centro) == 1:
        print("El centro del grafo es único.")
    else:
        print("El centro del grafo no es único.")

    print("Grafo Estrellado:")
    objeto_grafo.visualizar()
    
    centro_estrellado = objeto_grafo.centro()
    print("Centro del Grafo Estrellado:", centro_estrellado)
    
    grafo_completo = Grafo()

    # Insertar nodos
    nodos = ["A", "B", "C", "D"]
    vertices = [grafo_completo.insertar_vertice(nodo) for nodo in nodos]

    # Insertar aristas entre todos los nodos
    for i in range(len(vertices)):
        for j in range(i + 1, len(vertices)):
            grafo_completo.insertar_arista(vertices[i], vertices[j])

    print("Grafo Completo:")
    grafo_completo.visualizar()
    
    centro_completo = grafo_completo.centro()
    print("Centro del Grafo Completo:", centro_completo)


    grafo_arbol = Grafo()

    # Insertar nodos
    nodos_arbol = ["Raíz", "A", "B", "C", "D"]
    vertices_arbol = [grafo_arbol.insertar_vertice(nodo) for nodo in nodos_arbol]

    # Insertar aristas para formar un árbol
    grafo_arbol.insertar_arista(vertices_arbol[0], vertices_arbol[1])  # Raíz -> A
    grafo_arbol.insertar_arista(vertices_arbol[0], vertices_arbol[2])  # Raíz -> B
    grafo_arbol.insertar_arista(vertices_arbol[1], vertices_arbol[3])  # A -> C
    grafo_arbol.insertar_arista(vertices_arbol[1], vertices_arbol[4])  # A -> D

    print("Grafo de Árbol:")
    grafo_arbol.visualizar()

    centro_arbol = grafo_arbol.centro()
    print("Centro del Grafo de Árbol:", centro_arbol)

  
    centro_estrellado = objeto_grafo.centro()
    if len(centro_estrellado) == 1:
        print("El centro del Grafo Estrellado es único.")
    else:
        print("El centro del Grafo Estrellado no es único.")

    centro_completo = grafo_completo.centro()
    if len(centro_completo) == 1:
        print("El centro del Grafo Completo es único.")
    else:
        print("El centro del Grafo Completo no es único.")

    centro_arbol = grafo_arbol.centro()
    if len(centro_arbol) == 1:
        print("El centro del Grafo de Árbol es único.")
    else:
        print("El centro del Grafo de Árbol no es único.")


