import unittest
from collections import deque
from binary_tree import BinaryNode

"""

4.5 Validate BST

  Implement a function to check if a binary tree is a binary
  search tree.

"""

# for a BST, all the nodes on the left should be less than
# the nodes on the right
# assume no duplicate values?

# pass down min value and max value
def is_validate_bst_dfs(root, min_value=None, max_value=None):
  if root is None:
    return True

  if (min_value and root.value <= min_value) or \
    (max_value and root.value > max_value):
    return False

  if (not is_validate_bst_dfs(root.left, min_value, root.value)) or \
    (not is_validate_bst_dfs(root.right, root.value, max_value)):
    return False
  return True

  
def is_validate_bst_bfs(root):
  queue = deque()
  queue.append((root, None, None)) # node, min_value, max_value
  while queue:
    node, min_value, max_value = queue.popleft()
    if (min_value and node.value <= min_value) or \
      (max_value and node.value > max_value):
      return False
    if node.left:
      queue.append((node.left, min_value, node.value))
    if node.right:
      queue.append((node.right, node.value, max_value))

  return True


def _gen_test_tree_1():
  """
  Is BST
         5
      5
  """
  tree = BinaryNode(5)
  tree.left = BinaryNode(5)
  return tree

def _gen_test_tree_2():
  """
  Is BST
          5
      3       7
    2   4    6  8
  1               9
  """
  tree = BinaryNode(5)
  tree.left = BinaryNode(3)
  tree.left.left = BinaryNode(2)
  tree.left.left.left = BinaryNode(1)
  tree.left.right = BinaryNode(4)
  tree.right = BinaryNode(7)
  tree.right.left = BinaryNode(6)
  tree.right.right = BinaryNode(8)
  tree.right.right.right = BinaryNode(9)
  return tree

def _gen_test_tree_3():
  """
  Not BST
         5
      1    7
    2  3  8  9
  """
  tree = BinaryNode(5)
  tree.left = BinaryNode(1)
  tree.left.left = BinaryNode(2)
  tree.left.right = BinaryNode(3)
  tree.right = BinaryNode(7)
  tree.right.left = BinaryNode(8)
  tree.right.right = BinaryNode(9)
  return tree

def _gen_test_tree_4():
  """
  Not BST
          5
      3       9
    2   10    6  8       
  """
  tree = BinaryNode(5)
  tree.left = BinaryNode(3)
  tree.left.left = BinaryNode(2)
  tree.left.right = BinaryNode(10)
  tree.right = BinaryNode(9)
  tree.right.left = BinaryNode(6)
  tree.right.right = BinaryNode(8)
  return tree

def _gen_test_tree_5():
  """
  Not BST
        30
           30
  """
  tree = BinaryNode(30)
  tree.right = BinaryNode(30)
  return tree

def _gen_test_tree_6():
  """
  Not BST
        20
    10      30
      25
  """
  tree = BinaryNode(20)
  tree.left = BinaryNode(10)
  tree.right = BinaryNode(30)
  tree.left.right = BinaryNode(25)
  return tree

test_cases = [
  # test cases
  (_gen_test_tree_1, True),
  (_gen_test_tree_2, True),
  (_gen_test_tree_3, False),
  (_gen_test_tree_4, False),
  (_gen_test_tree_5, False),
  (_gen_test_tree_6, False),
]

test_functions = [
  # test functions
  is_validate_bst_dfs,
  is_validate_bst_bfs,
]

def test():
  for tree_gen, expected in test_cases:
    for test_func in test_functions:
      try:
        assert test_func(tree_gen()) == expected, "Failed"
      except AssertionError as e:
        e.args += (test_func.__name__, tree_gen.__name__, "should be " + str(expected))
        raise
  print("passed")

if __name__ == "__main__":
  test()