class Arbol_binario():
    
    class Nodo():
        def __init__(self, data, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right

    def __init__(self, root=None):
        self.root = root
        self.size = 0
        self.high = 0

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