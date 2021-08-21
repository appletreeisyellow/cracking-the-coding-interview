import unittest
from linked_list import LinkedList

"""

2.6 Palindrome

  Implement a function to check is a linked list is a palindrome.

"""

# Solution 1: hash table
def is_palindrome(ll):
  # use a hash table, store the count of each character
  # the linked list is a palindrome is at most one character is odd
  if ll is None:
    return True

  table = {}
  current = ll.head
  while current:
    if current.value not in table:
      table[current.value] = 1
    else:
      table[current.value] += 1
    current = current.next

  count_odd = 0
  for key in table:
    if table[key] % 2 == 1:
      count_odd += 1

  return count_odd <= 1


# Solution 2: reverse and compare
# Solution 3: iterative approach
#   reverse the first half and use stack
# Solution 4: recursive approach
# Check solution 2 - 4 on the book

class Test(unittest.TestCase):
  test_cases = [
    # add test cases here, ("test-case", True)
    ([1, 2, 2, 1], True),
    ([1], True),
    ([1, 1], True),
    ([1, 2], False),
    ([], True),
  ]
  test_functions = [
    # add testing functions here
    is_palindrome,
  ]

  def test(self):
    for values, expected in self.test_cases:
      for test_func in self.test_functions:
        try:
          result = test_func(LinkedList(values))
          assert (result == expected), "Failed!"
        except AssertionError as e:
          e.args += (test_func.__name__, values, "should be " + str(expected))
          raise


if __name__ == "__main__":
  unittest.main()