import unittest

"""

1.8 Zero Matrix

  Write an algorithm such that if an element in an MxN matrix is 0,
  it's entire row and column are set to 0.

"""

def zero_matrix(matrix):
  if len(matrix) == 0:
    return []

  m = len(matrix[0]) # number of columns
  n = len(matrix) # number of rows
  rows = set()
  cols = set()

  for x in range(n):
    for y in range(m):
      if matrix[x][y] == 0:
        rows.add(x)
        cols.add(y)

  for x in range(n):
    for y in range(m):
      if (x in rows) or (y in cols):
        matrix[x][y] = 0

  return matrix


class Test(unittest.TestCase):
  test_cases = [
    # add test cases here, ("test-case", True)
    # no zero
    ([[3, 3, 2],
      [3, 1, 3],
      [3, 3, 3]], [
      [3, 3, 2],
      [3, 1, 3],
      [3, 3, 3]]),
    # one zero
    ([[1, 3, 0],
      [4, 6, 4]], [
      [0, 0, 0],
      [4, 6, 0]]),
    # two zeros
    ([[1, 2, 2],
      [0, 2, 2],
      [0, 2, 2]], [
      [0, 2, 2],
      [0, 0, 0],
      [0, 0, 0]]),
    ([], []),
    ([[1], [0]], [[0], [0]]),
  ]
  test_functions = [
    # add testing functions here
    zero_matrix,
  ]

  def test(self):
    for text, expected in self.test_cases:
      for test_func in self.test_functions:
        try:
          assert (test_func(text) == expected), "Failed!"
        except AssertionError as e:
          e.args += (test_func.__name__, text, "should be " + str(expected))
          raise


if __name__ == "__main__":
  unittest.main()