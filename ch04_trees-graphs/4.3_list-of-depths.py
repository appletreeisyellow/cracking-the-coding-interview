import unittest
from collections import deque
from ch02_linked-lists.linked_list import LinkedList


"""

4.3 List of Depths

  Given a binary tree, design an algorithm which creates a linked
  list of all the nodes at each depth (e.g. if you have a tree with
  depth D, you'll have D linked lists).

"""

class BinaryNode:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

def create_list_by_depth_recursive(root):
  # recursive, pass down which level it is
  # put each linked_list in a table
  # merge the table for each level return from below
  pass
  
def create_list_by_depth_bfs(root):
  # BFS
  queue = deque()
  queue.append((root, 0))
  levels = {}
  while queue:
    node, level = queue.popleft()
    if level not in levels:
      # first node in level
      levels[level] = LinkedList()
    # node already exist
    levels[level].add(node)

    # push onto queue
    if node.left:
      queue.append((node.left, level + 1))
    if node.right:
      queue.append((node.right, level + 1))
  return levels


class Test(unittest.TestCase):
  test_functions = [
    #create_list_by_depth_recursive,
    create_list_by_depth_bfs,
  ]

  def test(self):
    """
          0
      1       2
    3  4     5  6
    """
    root = BinaryNode(0)
    root.left = BinaryNode(1)
    root.right = BinaryNode(2)
    root.left.left = BinaryNode(3)
    root.left.right = BinaryNode(4)
    root.right.left = BinaryNode(5)
    root.right.right = BinaryNode(6)

    for test_func in self.test_functions:
      levels = test_func(root)
      print(levels)
       
if __name__ == "__main__":
  unittest.main()