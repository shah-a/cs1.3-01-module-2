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

if __name__ == '__main__':
  test_prepend()
  print("`prepend()` tests passed")

  test_find()
  print("`find()` tests passed")

  test_delete()
  print("`delete()` tests passed")

  test_delete_v2()
  print("`delete()` tests (v2) passed")
