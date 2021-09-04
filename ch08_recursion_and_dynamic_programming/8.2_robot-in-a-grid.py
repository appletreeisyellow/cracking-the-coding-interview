import unittest

"""

8.2 Robot in a Grid

  Imagine a robot sitting on the upper left corner of grid with
  r rows and c columns. The robot can only move in two directions,
  right and down, but certain cells are "off limits" such that the
  robot cannot step on them. Design an algorithm to find a path for
  the robot from the top left to the bottom right.

"""

# without memorization
#  O(2^(r+c)) since each path has r+c steps and there are
#  two choices we can make at each step
def robot_in_a_grid_1(grid):
  if grid is None or len(grid) == 0 or len(grid[0]) == 0:
    return None
  path = []
  if has_path(grid, len(grid) - 1, len(grid[0]) - 1, path):
    return path
  return None

def has_path(grid, row, col, path):
  # if out of bound or not available, no path
  if (
    row < 0 or col < 0
    or row >= len(grid) or col >= len(grid[0])
    or grid[row][col] == 1
  ):
    return False

  # add to path if it is the origin, or valid path
  is_at_origin = (row == 0) and (col == 0)

  if (
    is_at_origin
    or has_path(grid, row - 1, col, path)
    or has_path(grid, row, col - 1, path)
  ):
    path.append((row, col))
    return True

  return False


# with memorization
def robot_in_a_grid_2(grid):
  if grid is None or len(grid) == 0 or len(grid[0]) == 0:
    return None

  path = []
  failed_points = set() # the points doesn't have path
  if has_path_memo(grid, len(grid) - 1, len(grid[0]) - 1, \
   path, failed_points):
    return path

  return None


def has_path_memo(grid, row, col, path, failed_points):
  # if out of boundary or the point is not available, no path
  if (
    row < 0 or col < 0
    or row >= len(grid) or col >= len(grid[0])
    or grid[row][col] == 1
  ):
    return False

  # if the point is in the failed_points, no path
  if (row, col) in failed_points:
    return False

  # if there is a path, add the point to the path and return True
  is_at_origin = (row == 0) and (col == 0)
  if (
    is_at_origin
    or has_path_memo(grid, row - 1, col, path, failed_points)
    or has_path_memo(grid, row, col - 1, path, failed_points)
  ):
    path.append((row, col))
    return True

  # else, add the point to the failed_points
  failed_points.add((row, col))
  return False


class Test(unittest.TestCase):
  test_cases = [
    # add test cases here, ("test-case", True)
    ([[0, 0, 0, 0],
      [0, 1, 1, 0],
      [0, 0, 0, 1],
      [1, 1, 0, 0]], 
      [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (3, 2), (3, 3)]),
    # path involve up direction
    ([[0, 1, 0, 0, 0],
      [0, 1, 0, 1, 0],
      [0, 0, 0, 1, 0],
      [1, 1, 1, 0, 0]], None),
    # path involve left direction
    ([[0, 1, 0, 0, 0],
      [0, 1, 0, 1, 0],
      [0, 0, 0, 1, 0],
      [1, 1, 1, 0, 0]], None),
    # no grid
    (None, None),
    # empty grid
    ([], None),
  ]
  test_functions = [
    # add testing functions here
    robot_in_a_grid_1,
    robot_in_a_grid_2,
  ]

  def test(self):
    for test_func in self.test_functions:
      for values, expected in self.test_cases:
        try:
          result = test_func(values)
          assert (result == expected), "Failed!"
        except AssertionError as e:
          e.args += (test_func.__name__, values, "should be " + str(expected))
          raise


if __name__ == "__main__":
  unittest.main()