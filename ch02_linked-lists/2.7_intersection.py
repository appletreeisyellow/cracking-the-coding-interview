import unittest
from linked_list import LinkedList

"""

2.7 Intersection

  Given two (singly) linked list, determine if the two lists
  intersect. Return the intersecting node. Note that the
  intersection is defined based on reference, not value. That is,
  if the kth node of the first linked list is the exact same node
  (by reference) as the jth node of the second linked list, then
  they are intersecting.

"""

def intersection_node(ll1, ll2):
  # chop off the extra nodes in the longer linked list
  # compare each node to check if there is any intersection

  # 1. find the length of each linked list and the tails
  # 2. if the tails are different by reference, return immediately
  #    there is no intersection
  # 3. set two pointers to the start of each linked list
  # 4. on the longer linked list, advance its pointer by the length diff
  # 5. traverse on each linked list until the pointers are the same

  if ll1.tail != ll2.tail:
    return None

  length1 = len(ll1)
  length2 = len(ll2)
  c1 = ll1.head
  c2 = ll2.head

  if length1 > length2: # chop off c1
    diff = length1 - length2
    while diff > 0:
      c1 = c1.next
      diff -= 1
  elif length2 > length1: # chop off c2
    diff = length2 - length1
    while diff > 0:
      c2 = c2.next
      diff -= 1

  while c1 is not c2:
    c1 = c1.next
    c2 = c2.next

  return c1


class Test(unittest.TestCase):
  same_node = LinkedList([1, 2, 3])
  ll1 = LinkedList([4, 3])
  ll2 = LinkedList([2, 6, 3, 2])
  ll1.tail.next = same_node.head
  ll1.tail = same_node.tail
  ll2.tail.next = same_node.head
  ll2.tail = same_node.tail
  expected = same_node
  
  test_cases = [
    # add test cases here, ("test-case", True)
    # no intersection
    (LinkedList([]), LinkedList([1]), None),
    (LinkedList([3, 1, 5, 9, 7, 2, 1]), LinkedList([4, 6, 7, 2, 1]), None),
    # has intersection
    (ll1, ll2, expected.head),
  ]
  test_functions = [
    # add testing functions here
    intersection_node,
  ]

  def test(self):
    for l1, l2, expected in self.test_cases:
      for test_func in self.test_functions:
        try:
          result = test_func(l1, l2)
          assert (result == expected), "Failed!"
        except AssertionError as e:
          e.args += (test_func.__name__, l1.values(), l2.values(), "should be " + str(expected))
          raise

if __name__ == "__main__":
  unittest.main()