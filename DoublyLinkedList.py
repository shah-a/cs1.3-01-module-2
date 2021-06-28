class Node:
    """Node class for linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    def __str__(self):
        return f"<Node, data: {self.data}>"

    def __repr__(self):
        return f"<Node, data: {self.data}>"

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def get_previous(self):
        return self.previous

    def set_data(self, data):
        self.data = data
    
    def set_next(self, data):
        self.next = data

    def set_previous(self, data):
        self.previous = data

class DoublyLinkedList:
    """Implements a doubly linked list."""
    def __init__(self):
        self.head = None
        self.len = 0

    def __str__(self):
        return f"<DoublyLinkedList, head: {self.head}>"

    def __repr__(self):
        return f"<DoublyLinkedList, head: {self.head}>"

    def is_empty(self):
        return self.head == None

    def size(self):
        return self.len

    def add(self, item):
        """In this implementation, `add` is used to prepend."""
        temp = Node(item)
        temp.set_next(self.head)
        if self.head != None:
            self.head.set_previous(temp)
        self.head = temp
        self.len += 1

    def search(self, item):
        current = self.head
        while current != None:
            if current.get_data() == item:
                return True
            current = current.get_next()
        return False

    def remove(self, item):
        current = self.head
        next = self.head.get_next()
        previous = self.head.get_previous()
        while current != None:
            if current.get_data() == item and previous != None:
                previous.set_next(current.get_next())
                if next: next.set_previous(previous)  # Check if `next` exists in case `item` is at the tail
                self.len -= 1
                break
            if current.get_data() == item and previous == None:
                if next: next.set_previous(None)  # Check if `next` exists in case `item` is at the tail
                self.head = next
                self.len -= 1
                break
            previous = current
            current = next
            next = next.get_next()

if __name__ == '__main__':
    my_ll = DoublyLinkedList()
    my_ll.add(31)
    print(my_ll)
