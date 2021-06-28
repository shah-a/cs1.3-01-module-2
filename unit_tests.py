from LinkedList import LinkedList
from DoublyLinkedList import DoublyLinkedList

def test_prepend():
  my_ll = LinkedList()

  my_ll.append(10)
  my_ll.append(20)
  my_ll.append(30)
  my_ll.append(55)

  my_ll.prepend(100)

  assert my_ll.head.data == 100

def test_find():
  my_ll = LinkedList()

  my_ll.append(10)
  my_ll.append(20)
  my_ll.append(30)
  my_ll.append(55)
  target = my_ll.head.next
  assert my_ll.find(20) == target
  assert my_ll.find(200) is None

def test_delete():
  my_ll = LinkedList()

  my_ll.append(10)
  my_ll.append(20)
  my_ll.append(30)
  my_ll.append(55)

  my_ll.delete(30)
  assert my_ll.head.next.next.data == 55

def test_delete_v2():
  my_ll = LinkedList()
  my_ll.append(10)
  my_ll.delete(10)
  assert my_ll.head == None
  assert my_ll.tail == None

  my_ll = LinkedList()
  my_ll.append(10)
  my_ll.append(20)
  my_ll.delete(20)
  assert my_ll.head.data == 10
  assert my_ll.tail.data == 10

  my_ll = LinkedList()
  my_ll.append(10)
  my_ll.append(20)
  my_ll.delete(10)
  assert my_ll.head.data == 20
  assert my_ll.tail.data == 20

def test_doubly_linked_list():
  my_ll = DoublyLinkedList()

  my_ll.add(31)
  my_ll.remove(31)
  assert my_ll.size() == 0

  my_ll.add(31)
  my_ll.add(77)
  my_ll.add(17)
  my_ll.add(93)
  my_ll.add(26)
  my_ll.add(54)
  assert my_ll.head.get_next().get_next().get_data() == 93
  assert my_ll.head.get_next().get_next().get_next().get_data() == 17
  assert my_ll.head.get_next().get_next().get_previous().get_data() == 26
  assert my_ll.size() == 6
  assert my_ll.search(93) == True
  assert my_ll.search(100) == False

  my_ll.add(100)
  assert my_ll.search(100) == True
  assert my_ll.size() == 7

  my_ll.remove(54)
  assert my_ll.size() == 6

  my_ll.remove(31)
  assert my_ll.size() == 5

  my_ll.remove(93)
  assert my_ll.size() == 4
  assert my_ll.search(93) == False

if __name__ == '__main__':
  test_prepend()
  print("`prepend()` tests passed")

  test_find()
  print("`find()` tests passed")

  test_delete()
  print("`delete()` tests passed")

  test_delete_v2()
  print("`delete()` tests (v2) passed")

  test_doubly_linked_list()
  print("DoublyLinkedList tests passed")
