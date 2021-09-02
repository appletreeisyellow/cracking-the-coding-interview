import unittest
from collections import deque
from binary_tree import BinaryNode

"""

4.7 Build Order

  You are given a list of projects and a list of dependencies (which
  is a list of pairs of projects, where the second project is
  dependent on the first project). All of a project's dependencies
  must be built before the project is. Find a build order that will
  allow the projects to be built. If there is no valid build order,
  return an error.

  EXAMPLE

  Input:
    projects: a, b, c, d, e, f
    dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)
  Output: f, e, a, b, d, c

"""

# build a graph
# if find a loop, return an error


def _gen_test_tree_1():
  pass

def _gen_test_tree_2():
  pass

def _gen_test_tree_3():
  pass

def _gen_test_tree_4():
  pass

test_cases = [
  # test cases
]

test_functions = [
  # test functions
]

def test():
  for tree_gen, expected in test_cases:
    for test_func in test_functions:
      try:
        assert test_func(tree_gen()) == expected, "Failed"
      except AssertionError as e:
        e.args += (test_func.__name__, tree_gen.__name__, "should be " + str(expected))
        raise

if __name__ == "__main__":
  test()