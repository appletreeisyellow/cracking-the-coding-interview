import unittest

"""

10.3 Search in Rotated Array

  Given a sorted array of n integers that has been rotated an unknown
  number of times, write code to find an element in the array. You may
  assume that the array was originally sorted in increasing order.

  EXAMPLE

  Input: find 5 in {15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14}
  Output: 8 (the index of 5 in the array)

"""

def search_in_rotated_array(array, target):
  return search_in_rotated_array_helper(array, target, 0, len(array)-1)

def search_in_rotated_array_helper(array, target, start, end):
  mid = (start + end) // 2
  
  if target == array[mid]:
    return mid

  if start > end:
    return -1

  """
    Either the left or right half must be normally ordered.
    Find out which side is normally ordered, and then use the
    normally ordered half to figure out which side to search to find x.
  """
  if array[start] < array[mid]:
    # the left side is ordered normally
    if target >= array[start] and target < array[mid]:
      # search left
      return search_in_rotated_array_helper(array, target, start, mid - 1)
    else:
      # search right
      return search_in_rotated_array_helper(array, target, mid + 1, end)
  elif array[mid] < array[start]:
    # the right side is ordered normally
    if target > array[mid] and target < array[end]:
      # search right
      return search_in_rotated_array_helper(array, target, mid + 1, end)
    else:
      # search left
      return search_in_rotated_array_helper(array, target, start, mid - 1)
  elif array[start] == array[mid]:
    if array[mid] != array[end]:
      # search right
      return search_in_rotated_array_helper(array, target, mid + 1, end)
    else:
      # we have to search both halves
      result = search_in_rotated_array_helper(array, target, start, mid - 1)
      if result == -1:
        return search_in_rotated_array_helper(array, target, mid + 1, end)
      else:
        return result

  return -1


class Test(unittest.TestCase):
  test_cases = [
    # add test cases here, ("test-case", True)
    ([3, 4, 5, 6, 1, 2], 1, 4),
    ([2, 2, 2, 3, 4, 2], 4, 4),
    ([4, 5, 1, 2, 3], 5, 1),
    ([15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], 5, 8),
  ]
  test_functions = [
    # add testing functions here
    search_in_rotated_array,
  ]

  def test(self):
    for test_func in self.test_functions:
      for values, target, expected in self.test_cases:
        try:
          result = test_func(values, target)
          assert (result == expected), "Failed!"
        except AssertionError as e:
          e.args += (test_func.__name__, values, "should be " + \
            str(expected) + ", but got " + str(result))
          raise


if __name__ == "__main__":
  unittest.main()