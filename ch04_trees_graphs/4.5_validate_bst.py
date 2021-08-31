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

def is_validate_bst_dfs(root):
  if root is None:
    return True

  if root.left:
    if root.left.value > root.value:
      return False
      
  if root.right:
    if root.right.value < root.value:
      return False

  return is_validate_bst_dfs(root.left) and is_validate_bst_dfs(root.right)
  
def is_validate_bst_bfs(root):
  if root is None:
    return True

  queue = deque()
  queue.append(root)
  while queue:
    node = queue.popleft()
    if node.left:
      if node.left.value < node.value:
        queue.append(node.left)
      else:
        return False
    if node.right:
      if node.right.value > node.value:
        queue.append(node.right)
      else:
        return False
  return True


def _gen_test_tree_1():
  """
  Is BST
         5
      1    7
    0  3  6  9
  """
  tree = BinaryNode(5)
  tree.left = BinaryNode(1)
  tree.left.left = BinaryNode(0)
  tree.left.right = BinaryNode(3)
  tree.right = BinaryNode(7)
  tree.right.left = BinaryNode(6)
  tree.right.right = BinaryNode(9)
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
    2   4    6  8
     0         
  """
  tree = BinaryNode(5)
  tree.left = BinaryNode(3)
  tree.left.left = BinaryNode(2)
  tree.left.left.right = BinaryNode(0)
  tree.left.right = BinaryNode(4)
  tree.right = BinaryNode(9)
  tree.right.left = BinaryNode(6)
  tree.right.right = BinaryNode(8)
  return tree

test_cases = [
  # test cases
  (_gen_test_tree_1, True),
  (_gen_test_tree_2, True),
  (_gen_test_tree_3, False),
  (_gen_test_tree_4, False),
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