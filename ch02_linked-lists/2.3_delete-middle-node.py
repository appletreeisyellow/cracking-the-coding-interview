import unittest
from linked_list import LinkedList

"""

2.3 Delete Middle Node

  Implement an algorithm to delete a node in the middle (i.e. any
  node but the first and last node, not necessarily the exact middle)
  of a singly linked list, given only access to that node.

  EXAMPLE
  Input: the node c from the linked list a->b->c->d->e->f
  Result: nothing is returned, but the new linked list looks
    like a->b->d->e->f
"""

def delete_middle_node(node_to_delete):
  # because the problem did give the head of the node,
  # so just copy the next code over and delete the next node
  if node_to_delete is None or node_to_delete.next is None:
    return False
  next_node = node_to_delete.next
  node_to_delete.value = next_node.value
  node_to_delete.next = next_node.next
  return True


class Test(unittest.TestCase):
  ll = LinkedList()
  ll.add_multiple(["a", "b", "c"])
  midlle_node = ll.add("d")
  ll.add_multiple(["e", "f"])
  last_node = ll.add("g")
  print(ll)
  test_cases = [
    (midlle_node, True),
    (last_node, False),
  ]
  for test, expected in test_cases:
    try:
      result = delete_middle_node(test)
      assert (result == expected), "Failed!"
    except AssertionError as e:
      e.args += (test, "should be " + str(expected))
      raise


if __name__ == "__main__":
  unittest.main()