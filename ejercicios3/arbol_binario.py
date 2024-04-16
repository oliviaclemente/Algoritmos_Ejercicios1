class Arbol_binario():
    
    class Nodo():
        def __init__(self, data, left=None, right=None):
            self.data = data       #data: que almacena el dato asociado al nodo.
            self.left = left       #left: que apunta al hijo izquierdo del nodo.
            self.right = right     #right: que apunta al hijo derecho del nodo.

    def __init__(self, root=None):    
        self.root = root      #root: que apunta al nodo raíz del árbol.
        self.size = 0        #size: que representa el número de elementos en el árbol.
        self.high = 0        #high: que almacena la altura del árbol.

    def add_element(self):
        pass
    def remove_element(self):
        pass

if __name__ == '__main__':
    t = Arbol_binario()
    t.root = t.Nodo(0)
    t.root.left = t.Nodo(1)
    t.root.right = t.Nodo(2)

    print(t.root.data)
    print(t.root.left.data)
    print(t.root.right.data)