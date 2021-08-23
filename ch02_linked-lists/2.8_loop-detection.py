import unittest
from linked_list import LinkedList

"""

2.8 Loop Detection

  Given a circular linked list, implement an algorithm that
  returns the node at the beginning of the loop.

  DEFINATION

  Circular linked list: A (corrupt) linked list in which a
  node's next pointer points to an earlier node, so as to
  make a loop in the linked list

  EXAMPLE

  InputL  A -> B -> C -> D -> E -> C [the same C as earlier]
  Output: C

"""

"""
Thoughts
1. do they collide? check using a fast pointer (two nodes
   a time) and a slow pointer (1 node a time)
2. when they collide, they are k nodes away from the start
   start of the loop
3. set one pointer at beginning and keep the other pointer
   at the collision node, move each pointer one node a time
   the node that they meet is the beginning of the loop
"""

def loop_detection(ll):
  fast_pt = ll.head
  slow_pt = ll.head
  while fast_pt and fast_pt.next:
    fast_pt = fast_pt.next.next
    slow_pt = slow_pt.next
    if fast_pt is slow_pt:
      # collision node
      break
  
  if fast_pt is None or fast_pt.next is None:
    return None

  fast_pt = ll.head
  while fast_pt is not slow_pt:
    fast_pt = fast_pt.next
    slow_pt = slow_pt.next

  return fast_pt

class Test(unittest.TestCase):
  loop = LinkedList([1, 3, 4, 2, 5])
  loop_start_node = loop.head.next.next
  loop.tail.next = loop_start_node
  test_cases = [
    # add test cases here, ("test-case", True)
    (LinkedList([]), None),
    (LinkedList([1, 2, 3]), None),
    (loop, loop_start_node),
  ]
  test_functions = [
    # add testing functions here
    loop_detection,
  ]

  def test(self):
    for values, expected in self.test_cases:
      for test_func in self.test_functions:
        try:
          result = test_func(values)
          assert (result == expected), "Failed!"
        except AssertionError as e:
          e.args += (test_func.__name__, values.values(), "should be " + str(expected))
          raise


if __name__ == "__main__":
  unittest.main()