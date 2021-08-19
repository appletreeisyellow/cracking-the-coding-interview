import unittest
from linked_list import LinkedList

"""

2.2 Return Kth to Last

  Implement an algorithm to find the kth to last element of 
  a singly linked list.

"""

# 1. put linked list into a(n) list/array
# 2. use two pointers

def return_kth_to_last_1(ll, k):
  if k <= 0:
    return None

  array = []
  current = ll.head
  while current:
    array.append(current.value)
    current = current.next
  
  if k > len(array):
    return None
  
  idx = len(array) - k
  return array[idx]

def return_kth_to_last_2(ll, k):
  if k < 0:
    return None
  # p2 and p1 are kth element apart
  # p2 is closer to the tail
  p1 = ll.head
  p2 = ll.head 
  count = 0
  while p2:
    p2 = p2.next
    count += 1
    if count == k:
      break
  if count != k:
    return None
  # move p1 and p2 together until p2 hit the end
  while p1 and p2:
    p1 = p1.next
    p2 = p2.next
  return p1.value


class Test(unittest.TestCase):
  test_cases = [
    # add test cases here, ("test-case", True)
    ([2, 3, 4, 4], 3, 3),
    ([2, 3, 4, 1], 2, 4),
    ([2, 3, 4, 1], 0, None),
    ([2, 3, 4, 4], 5, None),

  ]
  test_functions = [
    # add testing functions here
    return_kth_to_last_1,
    return_kth_to_last_2,
  ]

  def test(self):
    for values, k, expected in self.test_cases:
      for test_func in self.test_functions:
        try:
          result = test_func(LinkedList(values), k)
          assert (result == expected), "Failed!"
        except AssertionError as e:
          e.args += (test_func.__name__, values, "should be " + str(expected))
          raise


if __name__ == "__main__":
  unittest.main()