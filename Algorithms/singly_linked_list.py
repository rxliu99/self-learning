"""
Algorithm - Linked List
Reference:
    - https://www.youtube.com/watch?v=8hly31xKli0
    - https://teamtreehouse.com/library/introduction-to-data-structures/building-a-linked-list/singly-and-doubly-linked-lists-2
    - https://teamtreehouse.com/library/introduction-to-data-structures/building-a-linked-list/linked-lists-operations
Last edited: 2022-08-20
"""

### Singly Linked List ###
# Can be traversed in only one direction from head to the last node (tail)
# Each node contains data and a pointer to the next node

class Node:
    """
    An object for storing a single node in a linked list

    Attributes:
        data: Data stored in node
        next_node: Reference to next node in linked list
    """
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data
        self.next_node = next_node

    def __repr__(self):
        return "<Node data: %s>" % self.data

class SinglyLinkedList:
    """
    Linear data structure that stores values in nodes. 
    The list maintains a reference to the first node, also called head. 
    Each node points to the next node in the list

    Attributes:
        head: The head node of the list

    Methods:
        is_empty()
        size()
        prepend(data)
        search(target)
        search_index(index)
        insert(data, index)
        remove(target)
        remove_index(index)
    """
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        """
        Check if the linked list is empty
        Takes O(1) time
        """
        return self.head == None
    
    def size(self):
        """
        Calculate the number of nodes contained in the linked list.
        Takes O(n) time
        """
        current = self.head
        counter = 0
        while current:
            counter += 1
            current = current.next_node
        return counter

    def prepend(self, data):
        """
        Prepend a new node containing data at the head of the linked list.
        Takes O(1) time
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node
    
    def search(self, target):
        """
        Search for the first node containing data that matches the target.
        Return the node or 'None' if not found.
        Takes O(n) time
        """
        current = self.head

        while current:
            if current.data == target:
                return current
            else:
                current = current.next_node
        return None

    def search_index(self, index):
        """
        Search for the Node at specified index.
        Takes O(n) time
        """
        if index >= self.size():
            raise IndexError('index out of range')
        
        if index == 0:
            return self.head
        else:
            current = self.head
            position = 0
            while position < index:
                current = current.next_node
                position += 1
        return current

    def insert(self, data, index):
        """
        Insert a new Node containing data at index position.
        Insertion takes O(1) time but finding node at insertion point takes
        O(n) time.
        Takes overall O(n) time
        """
        if index >= self.size():
            raise IndexError('index out of range')
        
        if index == 0:
            self.prepend(data)
        elif index > 0:
            new_node = Node(data)
            position = index
            current = self.head
            
            while position > 1:
                current = current.next_node
                position -= 1
            
            prev_n = current
            next_n = current.next_node

            prev_n.next_node = new_node
            new_node.next_node = next_n

    def remove(self, target):
        """
        Removes Node containing data that matches the target
        Returns the node or `None` if key doesn't exist
        Takes O(n) time
        """
        current = self.head
        prev_n = None
        found = False

        while current and not found:
            if (current.data == target) and (current is self.head):
                found = True
                self.head = current.next_node
                return current
            elif current.data == target:
                found = True
                prev_n.next_node = current.next_node
                return current
            else:
                prev_n = current
                current = current.next_node
    
        return None 
    
    def remove_index(self, index):
        """
        Removes Node at specified index
        Takes O(n) time
        """
        if index >= self.size():
            raise IndexError('index out of range')
        
        current = self.head

        if index == 0:
            self.head = current.next_node
            return current
        else:
            position = index

            while position > 1:
                position -= 1
                current = current.next_node

            prev_n = current
            current = current.next_node
            next_n = current.next_node

            prev_n.next_node = next_n
            return current 

    def __repr__(self):
        """
        Return a string representation of the list.
        Takes O(n) time
        """
        nodes = []
        current = self.head
        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)
            current = current.next_node
        return  ' -> '.join(nodes)
