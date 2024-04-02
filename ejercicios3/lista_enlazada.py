class Linkedlist:
    
    class Node:
        def __init__(self, element=None, next=None):    #constructuor
            self._element= element
            self._next= next
            
    a= Node(next=Node())
    a._element= 3
    a._next= Node()
    
            
    def __init__(self):
        self.head= None
        self.size= 0
        
    def __len__(self):
        return self.size
    
    def __str__(self):
        returning_value= '['
        if not self.is_empty():
            node=  self.head
            while node._next != None:
                returning_value += str(node._element)
        return returning_value + ']'


    def is_empty(self):
        return self.size == 0
    
    def add_first(self, element):
        new= self.Node(element, self.head)
        self.head= new
        self.size += 1
        
    def remove_first(self):
        if self.is_empty():
            raise IndexError("Empty List.")
        self.head= self.head._next
        self.size -= 1
        
    def add_last(self, element):
        node= node._next 
        node._next= new
        self.size +=1
        
if __name__ == '__main__':
    l_l= Linkedlist()
    print(l_l)
    print(l_l.head)
    print(len(l_l))
    for x in range(10):
        l_l.add_first(x)
    print(l_l)
        
    