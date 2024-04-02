class Binary_tree:
    
    class Node:
        def __init__(self, data, left=None, right=None):
            # self.parent = parent
            self.data = data
            self.left = left
            self.right = right

    def __init__(self):
        self.root = None
        self.size = 0
        # self.high = high

    def add_element(self, pnode, data):
        if pnode.left is None:
            pnode.left = self.Node(data)
            self.size += 1
        elif pnode.right is None:
            pnode.right = self.Node(data)
            self.size += 1
        else:
            raise IndexError("The node is full.")
        
    def add_element_as_child(self, pnode, data, pos = 'l'):
        if pos == 'l':
            pnode.left = self.Node(data)
            self.size += 1
        elif pos == 'r':
            pnode.right = self.Node(data)
            self.size += 1
        else:
            raise IndexError("")
    
    def children(self, node):
        return [node.left, node.right]
    
    def search_preorder(self, x, node=None):
        if node is None:
            node = self.root

        if node == x:
            return node
        
        for c in self.children(node):
            if c is not None:
                self.search_preorder(x, c)

    def search_inorder(self, x, node=None):
        if node is None:
            node = self.root

        if node.left is not None:
            self.search_inorder(x, node.left)

        if node == x:
            return node

        elif node.right is not None:
            self.search_inorder(x, node.right)


        
        


if __name__ == '__main__':
    t = Binary_tree()
    print(t.size)
    t.size = 10
    print(t.size)