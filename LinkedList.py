class Node:

  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:

  '''Implements a basic singly linked list'''

  def __init__(self):

    #head and tail references
    #point to node at start and end
    self.head = None
    self.tail = None

  def append(self, data):
    '''Add a new node to the end of the linked list'''

    #create a new node with the given data
    new_node = Node(data)

    #what if my linked list is empty?
    if self.head is None:
      #set the head and tail to the new node
      self.head = new_node
      self.tail = new_node
      return

    #make the tail next ptr point at the new node
    #to make a new link use variable assignment!
    self.tail.next = new_node

    #make the tail point at the new node
    self.tail = new_node

  def prepend(self, data):
    '''Add a new node to the beginning of the linked list'''
    pass

  def delete(self, item):
    '''Remove a specific data item from the linked list'''
    pass

  def find(self, item):
    '''Find a specific item in the linked list, return the node, if not found return None'''
    pass

  def print_list(self):
    
    #TODO: try to implement 
    #start with the head
    current = self.head

    #keep going until we hit None at the end of the LL
    while current is not None:

      #print the data of the node we are visiting
      print(current.data)

      #most important piece! move current via reassignment to point at the next node
      current = current.next
