from LinkedList import LinkedList

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