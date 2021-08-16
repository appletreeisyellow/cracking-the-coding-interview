import unittest

"""

1.7 Rotate Matrix:

  Given an image represented by an NxN matrix, where each
  pixel in the image is 4 bytes, write a method to rotate
  the image by 90 degrees. Can you do this in place?

"""

def rotate_matrix(matrix):
  # assume the rotation is clock-wise
  
  if len(matrix) == 0 or len(matrix) != len(matrix[0]):
    return False

  n = len(matrix)
  for x in range(0, int(n/2)): # x is row
    for y in range(x, n-1-x): # y is column
      # save top
      tmp = matrix[x][y]
      # right -> top
      matrix[x][y] = matrix[y][n-1-x]
      # bottom -> right
      matrix[y][n-1-x] = matrix[n-1-x][n-1-y]
      # left -> bottom
      matrix[n-1-x][n-1-y] = matrix[n-1-y][x]
      # top -> left 
      matrix[n-1-y][x] = tmp

  return True



class Test(unittest.TestCase):
  test_cases = [
    # add test cases here, ("test-case", True)
    ([[1]], True),
    ([[1, 2],
      [3, 4]], True),
    ([[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]], True),
    ([[1,  2,  3,  4],
      [5,  6,  7,  8],
      [9,  10, 11, 12],
      [13, 14, 15, 16]], True),
    ([[1, 2]], False),
    ([], False),
    ([[1], [2]], False),
  ]
  test_functions = [
    # add testing functions here
    rotate_matrix,
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