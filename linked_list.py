class Node:
    """
    An Object for storing a single node of a linked list.
    Models two attributes - data and the link to the next node in
    the list.
    """

    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"<Node data: {self.data}>"


class LinkedList:
    """
    Singly linked list
    """
    def __init__(self):
        self.head = None 

    def is_empty(self):
        return self.head == None

    def size(self):
        """
        Returns the number of nodes in the list.
        Takes O(n) time.
        """

        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node
        
        return count

    def add(self, data):
        """
        Add new node Node containing data at the head of list.
        Takes o(1) time.
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        """
        Search for the first node cotaining data that matches the key.
        Return Noe or `None` if not found.
        Takes O(n) time.
        """
        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

    def insert(self, data, index):
        """
        Inserts a new Node containing data as index position.
        Insertion take O(1) time but finding the node as the insertion
        point takes O(n) time.

        Take overall O(n) time.
        """
        if index == 0:
            self.add(data)
        
        else:
            new_node = Node(data)

            posistion = index
            current = self.head

            while posistion > 1 and current.next_node:
                current = current.next_node
                posistion -= 1

            prev_node = current
            next_node = current.next_node


            prev_node.next_node = new_node
            new_node.next_node = next_node

    def remove(self, key):
        """
        Remove Node containing data that matches the key.
        Returns the node or None if key doesn't exist.
        Takes O(n) time.
        """
        current = self.head

        prev_node = None 
        found = False

        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True 
                prev_node.next_node = current.next_node
            else:
                prev_node = current
                current = current.next_node

        return current


    def __repr__(self):
        """
        Return a string representation of the list.
        Takes O(n) time.
        """

        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append(f"[Head: {current.data}]")
            elif current.next_node is None:
                nodes.append(f"[Tail: {current.data}]")
            else:
                nodes.append(f"[{current.data}]")
            
            current = current.next_node

        return "->".join(nodes)
        