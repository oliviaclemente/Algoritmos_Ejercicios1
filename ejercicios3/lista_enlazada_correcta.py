class LinkedList:
    
    class Node:      # clase interna Node, que representa un nodo de la lista enlazada.
        def __init__(self, element=None, next=None):    
            self._element = element     #_element, que almacena el elemento del nodo
            self._next = next           #_next, que apunta al siguiente nodo en la lista.

    def __init__(self):  
        self.head = None       # atributo head como None (indicando una lista vacía)
        self.size = 0          # el tamaño size como 0.

    def __len__(self):        #el tamaño de la lista enlazada
        return self.size      #representado por el atributo size.
    
    def __str__(self):     #Devuelve una representación en forma de cadena de la lista enlazada
        returning_value = '['         #Inicializa una cadena llamada returning_value
        if not self.is_empty():      #Comprueba si la lista enlazada está vacía usando el método is_empty
            node = self.head         #nicializa una variable node con el primer nodo (head) de la lista.
            returning_value += str(node._element)    #Agrega el elemento del primer nodo a returning_value
            while node._next != None:   #Itera sobre la lista enlazada moviéndote al siguiente nodo (_next) mientras este no sea None
                node = node._next
                returning_value += ', ' + str(node._element)     #cuando el siguiente nodo es None, se detiene el bucle y returning_value contiene todos los elementos de la lista enlazada separados por comas.
        return returning_value + ']'     #lista está vacía, el método simplemente devuelve returning_value
    
    def is_empty(self):          #Devuelve True si la lista está vacía, es decir, si el tamaño es 0.
        return self.size == 0   

    def add_first(self, element): #Agrega un nuevo elemento al principio de la lista.
        new = self.Node(element, self.head)    #Crea un nuevo nodo con el elemento proporcionado y lo enlaza al nodo actual head.
        self.head = new                      #Actualiza el atributo head para que apunte al nuevo nodo.
        self.size += 1                    #Incrementa el tamaño de la lista en 1.

    def remove_first(self):      #Elimina el primer elemento de la lista.
        if self.is_empty():
            raise IndexError("Empty list.")    #Si la lista está vacía, se levanta una excepción IndexError.
        self.head = self.head._next        #Actualiza el atributo head para que apunte al siguiente nodo.
        self.size -= 1                     #Decrementa el tamaño de la lista en 1.

    def add_last(self, element):       #Agrega un nuevo elemento al final de la lista.
        new = self.Node(element)
        node = self.head
        while node._next != None:    #Itera sobre la lista hasta encontrar el último nodo.
            node = node._next   
        node._next = new        #Crea un nuevo nodo con el elemento proporcionado y lo enlaza al último nodo encontrado.
        self.size += 1       #Incrementa el tamaño de la lista en 1.

if __name__ == '__main__':
    
    l_l = LinkedList()         # Se crea una nueva instancia de la clase LinkedList. Al ser recién creada, l_l es una lista enlazada vacía.
    print(l_l)                 
    print(l_l.head)          # Se imprime el atributo head de la lista enlazada
    print(len(l_l))        #imprime la longitud de la lista enlazada
    for x in range(10):       # Se ejecuta un bucle que agrega los números del 0 al 9 al principio de la lista enlazada.
        l_l.add_first(x)
        print(l_l)
    print(l_l)
    l_l.remove_first()    #Se elimina el primer elemento de la lista enlazada
    print(l_l)
    l_l.add_last('a')    #Se imprime la lista enlazada después de agregar 'a' al final
    print(l_l)