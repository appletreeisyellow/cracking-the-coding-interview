import time

"""

3.6 Animal Shelter

  An animal shelter, which holds only dogs and cats, operates on
  a strictly "first in, first out" basis. People must adopt either
  the "oldest" (based on arrival time) of all animal at the shelter,
  or they can select whether they would prefer a dog or a cat (and
  will receive the oldest animal of that type). They cannot select
  which specific animal they would like. Create the data structures
  to maintain this system and implement operations such as enqueue,
  dequeueAny, dequeueDog, and dequeueCat. You may use the built-in
  LinkedList data structure.

"""

class Node:
  def __init__(self, data, next_node=None):
    self.data = data
    self.next_node = next_node

  def __str__(self):
    return str(self.data)


class LinkedList:
  def __init__(self, head=None):
    self.head = head

  def insert(self, node):
    if self.head is None:
      self.head = node
      return
    
    current_node = self.head
    while current_node.next_node:
      current_node = current_node.next_node
    current_node.next_node = node

  def pop_head(self):
    if self.head is None:
      return None
    node = self.head
    self.head = self.head.next_node
    return node

  def peek(self):
    if self.head is None:
      return None
    return self.head

  def size(self):
    if self.head is None:
      return 0
    
    length = 0
    current_node = self.head
    while current_node:
      length += 1
      current_node = current_node.next_node
    return length

# Animal

class Animal:
  def __init__(self, name):
    self.time_arrived = time.time()
    self.name = name

  def get_time_arrived(self):
    return self.time_arrived

  def is_older_than(self, animal):
    return self.time_arrived < animal.get_time_arrived()

  def get_name(self):
    return self.name

class Dog(Animal):
  pass

class Cat(Animal):
  pass

class AnimalShelter:
  def __init__(self):
    self.cats = LinkedList()
    self.dogs = LinkedList()

  def enqueue(self, animal):
    if isinstance(animal, Cat):
      self.cats.insert(Node(animal))
    elif isinstance(animal, Dog):
      self.dogs.insert(Node(animal))

  def dequeue_any(self):
    # compare which is earlier
    dog = self.dogs.peek()
    cat = self.cats.peek()
    if dog is None and cat is None:
      return None
    elif dog is None:
      return self.dequeue_cat()
    elif cat is None:
      return self.dequeue_dog()

    if dog.is_older_than(cat):
      return self.dequeue_dog()
    
    return self.dequeue_cat()

  def dequeue_dog(self):
    return self.dogs.pop_head().data

  def dequeue_cat(self):
    return self.cats.pop_head().data

  def size(self):
    return self.cats.size() + self.dogs.size()


def test_animal_shelter():
  a = AnimalShelter()
  a.enqueue(Cat("Mona"))
  a.enqueue(Cat("Lisa"))
  a.enqueue(Dog("Sparky"))
  a.enqueue(Cat("Miao"))

  assert a.size() == 4
  mona = a.dequeue_cat()
  assert  mona.name == "Mona"
  sparky = a.dequeue_dog()
  assert  sparky.name == "Sparky"
  lisa = a.dequeue_any()
  assert lisa.name == "Lisa"
  
  print("passed")

if __name__ == "__main__":
  test_animal_shelter()