import unittest

"""

8.3 Magic Index

  A magic index in an array A [1. .. n -1] is defined to be 
  an index such that A[i] = i. Given a sorted array of distinct
  integers, write a method to find a magic index, if one exists,
  in array A.

  FOLLOW UP
  
  What if the values are not distinct?

"""

# binary search
# O(log2 n)
def find_magic_index(array):
  if array is None or len(array) == 0:
    return -1

  return find_magic_index_helper(array, 0, len(array) - 1)

def find_magic_index_helper(array, start, end):
  if start > end:
    return -1

  mid = (start + end) // 2 # middle index
  if array[mid] == mid:
    return mid
  elif array[mid] < mid:
    # search right half
    return find_magic_index_helper(array, mid + 1, end)
  else:
    # search left half
    return find_magic_index_helper(array, start, mid - 1)


def find_magic_index_follow_up(array):
  # e.g.
  # index:   0   1  2  3  4  5  6  7  8   9  10
  # value: -10  -5  2  2  2  3  4  7  9  12  13
  # A[5] = 3, we know that A[4] cannot be a magic index,
  #   but A[4] must be <= A[5]
  # Instead of search the whole left side, we search
  # A[0] to A[3] where 3 is the value of A[5]

  # if A[mid] < mid, search left [start, min(mid-1, mid_value)]
  # else, search right [max(mid+1, mid_value)]

  if array is None or len(array) == 0:
    return -1

  return find_magic_index_follow_up_helper(array, 0, len(array) - 1)

def find_magic_index_follow_up_helper(array, start, end):
  if start > end:
    return -1

  mid = (start + end) // 2
  mid_value = array[mid]

  if mid_value == mid:
    return mid

  # search left [start, min(mid-1, mid_value)]
  left = find_magic_index_follow_up_helper(array, start, min(mid - 1, mid_value))
  if left >=0:
    return left

  # search right [max(mid+1, mid_value)]
  return find_magic_index_follow_up_helper(array, max(mid + 1, mid_value), end)

class Test(unittest.TestCase):
  def test(self):
    test_cases = [
      # distinct values
      ([-40, -20, -1, 1, 2, 3, 5, 7, 9, 12, 13], 7),
      ([-4, -3, -2], -1),
      ([], -1),
    ]
    for values, expected in test_cases:
      try:
        result = find_magic_index(values)
        assert (result == expected), "Failed!"
      except AssertionError as e:
        e.args += ("find_magic_index", values, "should be " + \
          str(expected) + ", but got " + str(result))
        raise

  def test_follow_up(self):
    test_cases = [
      # distinct values
      ([-40, -20, -1, 1, 2, 3, 5, 7, 9, 12, 13], 7),
      ([-4, -3, -2], -1),
      ([], -1),
      # repeated values
      ([-10, -4, -2, 2, 2, 2, 4, 7, 7, 7], 7),
      ([-10, -4, 2, 2, 2, 2, 4, 7, 7, 7], 2),
    ]
    for values, expected in test_cases:      
      try:
        result = find_magic_index_follow_up(values)
        assert (result == expected), "Failed!"
      except AssertionError as e:
        e.args += ("find_magic_index_follow_up", values, "should be " + \
          str(expected) + ", but got " + str(result))
        raise

if __name__ == "__main__":
  unittest.main()