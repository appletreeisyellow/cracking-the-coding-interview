import unittest
from collections import deque
from binary_tree import BinaryNode

"""

4.4 Check Balanced

  Implement a function to check if a binary tree is balanced.
  For the purposes of this question, a balanced tree is defined
  to be a tree such that the heights of the two subtrees of any
  node never differ by more than one.

"""


def is_balanced_bfs(root):
  if root is None:
    return True

  min_depth = 10 ** 100
  max_depth = -10 ** 100
  queue = deque()
  queue.append((root, 0))
  visited = [root]
  while queue:
    node, curr_depth = queue.popleft()
    if node.left is None and node.right is None:
      if curr_depth > max_depth:
        max_depth = curr_depth
      if curr_depth < min_depth:
        min_depth = curr_depth
    else:
      if node.left and node.left not in visited:
        queue.append((node.left, curr_depth + 1))
        visited.append(node.left)
      if node.right and node.right not in visited:
        queue.append((node.right, curr_depth + 1))
        visited.append(node.right)
        
  return max_depth - min_depth < 2


# find the max depth and min depth
# the two depth should be the same
def is_balanced_by_depth(root):
  diff = find_max_depth(root) - find_min_depth(root)
  return diff < 2

def find_max_depth(node, level=0):
  if node is None:
    return level
  if not node.left:
    return find_max_depth(node.right, level + 1)
  if not node.right:
    return find_max_depth(node.left, level + 1)
  return max(find_max_depth(node.left, level + 1),
    find_max_depth(node.right, level + 1))

def find_min_depth(node, level=0):
  if node is None:
    return level
  if not node.left:
    return find_min_depth(node.right, level + 1)
  if not node.right:
    return find_min_depth(node.left, level + 1)
  return min(find_min_depth(node.left, level + 1),
    find_min_depth(node.right, level + 1))

def _gen_balanced_1():
  """
       0
    1     2
  3  4   5  6
7
  """
  tree = BinaryNode(0)
  tree.left = BinaryNode(1)
  tree.right = BinaryNode(2)
  tree.left.left = BinaryNode(3)
  tree.left.right = BinaryNode(4)
  tree.right.left = BinaryNode(5)
  tree.right.right = BinaryNode(6)
  tree.left.left.left = BinaryNode(7)
  return tree

def _gen_balanced_2():
  """
       0
    1     2
  3  4   5 
  """
  tree = BinaryNode(0)
  tree.left = BinaryNode(1)
  tree.right = BinaryNode(2)
  tree.left.left = BinaryNode(3)
  tree.left.right = BinaryNode(4)
  tree.right.left = BinaryNode(5)
  return tree

def _gen_unbalanced_1():
  """
       0
    1     2
  3  4
       5
  """
  tree = BinaryNode(0)
  tree.left = BinaryNode(1)
  tree.right = BinaryNode(2)
  tree.left.left = BinaryNode(3)
  tree.left.right = BinaryNode(4)
  tree.left.right.right = BinaryNode(5)
  return tree

def _gen_unbalanced_2():
  """
       0
    1     2
  3  4   5
           6
             7
  """
  tree = BinaryNode(0)
  tree.left = BinaryNode(1)
  tree.right = BinaryNode(2)
  tree.left.left = BinaryNode(3)
  tree.left.right = BinaryNode(4)
  tree.right.left = BinaryNode(5)
  tree.right.left.right = BinaryNode(6)
  tree.right.left.right.right = BinaryNode(7)
  return tree

test_cases = [
  (_gen_balanced_1, True),
  (_gen_balanced_2, True),
  (_gen_unbalanced_1, False),
  (_gen_unbalanced_2, False),
]

test_functions = [
  is_balanced_bfs,
  is_balanced_by_depth,
]

def test_is_balanced():
  for tree_gen, expected in test_cases:
    for test_func in test_functions:
      assert test_func(tree_gen()) == expected

if __name__ == "__main__":
  test_is_balanced()