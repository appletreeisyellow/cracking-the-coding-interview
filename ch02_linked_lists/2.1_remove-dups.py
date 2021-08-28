import unittest
from linked_list import LinkedList

"""

2.1 Remove Dups

  Write code to remove duplicates from an unsorted linked list.

  FOLLOW UP
  How would you solve this problem if a temporary buffer is not allowed?

"""

def remove_dups(input):
  # have a set, if a node is in set, then remove the node
  appeared = set()
  previous = None
  current = input.head
  while current != None:
    if current.value in appeared:
      previous.next = current.next
    else:
      appeared.add(current.value)
      previous = current
    current = current.next
  input.tail = previous
  return input


class Test(unittest.TestCase):
  test_cases = [
    # add test cases here, ("test-case", True)
    ([], []),
    ([1, 1, 1, 1, 1, 1], [1]),
    ([1, 2, 3, 2], [1, 2, 3]),
    ([1, 1, 2, 3], [1, 2, 3]),
    ([1, 2, 2, 3], [1, 2, 3]),
    ([1, 2, 3, ], [1, 2, 3]),
  ]
  test_functions = [
    # add testing functions here
    remove_dups,
  ]

  def test(self):
    for values, expected in self.test_cases:
      for test_func in self.test_functions:
        try:
          expected = expected.copy()
          deduped = test_func(LinkedList(values))
          assert (deduped.values() == expected), "Failed!"
          deduped.add(5)
          expected.append(5)
          assert (deduped.values() == expected), "Failed"
        except AssertionError as e:
          e.args += (test_func.__name__, values, "should be " + str(expected))
          raise


if __name__ == "__main__":
  unittest.main()