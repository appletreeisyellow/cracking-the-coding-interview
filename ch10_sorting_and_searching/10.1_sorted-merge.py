import unittest

"""

10.1 Sorted Merge

  You are given two sorted arrays, A and B, where A has a large
  enough buffer at the end to hold B. Write a method to merge B
  into A in sorted order.

"""

def sorted_merge(a, b):
  len_b = len(b)
  len_a = len(a) - len(b) # a has empty spaces at the end to hold b
  # starting from the end of each array

  # put the element at the end of the array if it is bigger

  b_idx = len_b - 1
  a_idx = len_a - 1
  last_index = len(a) - 1

  while b_idx >= 0 and a_idx >= 0:
    b_val = b[b_idx]
    a_val = a[a_idx]
    if b_val > a_val:
      a[last_index] = b_val
      b_idx -= 1
    else:
      a[last_index] = a_val
      a_idx -= 1
    last_index -= 1

  while b_idx >= 0:
    # copy b value into a
    a[last_index] = b[b_idx]
    last_index -= 1
    b_idx -= 1

  # if there is more value in a, then it is already sorted
  return a


class Test(unittest.TestCase):
  test_cases = [
    # add test cases here, ("test-case", True)
    ([1, 2, 3, None], [0], [0, 1, 2, 3]),
    ([3, 6, 8, 9, None, None], [0, 4], [0, 3, 4, 6, 8, 9]),
    ([4, None, None, None], [5, 6, 7], [4, 5, 6, 7]),
    ([2, 4, 6, None, None, None], [1, 3, 5], [1, 2, 3, 4, 5, 6]),
  ]
  test_functions = [
    # add testing functions here
    sorted_merge,
  ]

  def test(self):
    for test_func in self.test_functions:
      for a, b, expected in self.test_cases:
        try:
          result = test_func(a, b)
          assert (result == expected), "Failed!"
        except AssertionError as e:
          e.args += (test_func.__name__, a, b, "should be " + \
            str(expected) + ", but got " + str(result))
          raise


if __name__ == "__main__":
  unittest.main()