import unittest
import copy

"""

8.4 Power Set

  Write a method to return all subsets of a set.

"""

def power_set(array):
  n = len(array)
  if n == 0:
    return [[]]

  if n == 1:
    return [[], [array[0]]]

  # get the power_set(array[0...n-2])
  allsubsets = power_set(array[:n-1])
  item = array[n-1]
  moresubsets = []

  # merge power_set of array[0...n-2] and array[n-1]
  for subset in allsubsets:
    new_subset = copy.deepcopy(subset)
    new_subset.append(item)
    moresubsets.append(new_subset)
  allsubsets += moresubsets
  return allsubsets

  

class Test(unittest.TestCase):
  test_cases = [
    # add test cases here, ("test-case", True)
    ([], [[]]),
    ([1], [[], [1]]),
    ([1, 2], [[], [1], [2], [1, 2]]),
    ([1, 2, 3], [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]),
  ]
  test_functions = [
    # add testing functions here
    power_set,
  ]

  def test(self):
    for values, expected in self.test_cases:
      for test_func in self.test_functions:
        try:
          result = test_func(values)
          assert result == expected, "Failed!"
        except AssertionError as e:
          e.args += (test_func.__name__, values, "should be " + \
            str(expected) + ", but got " + str(result))
          raise


if __name__ == "__main__":
  unittest.main()