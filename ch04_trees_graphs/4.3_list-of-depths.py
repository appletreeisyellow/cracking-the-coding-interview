import unittest
from collections import deque
from binary_tree import BinaryNode
from ch02_linked_lists.linked_list import LinkedList


"""

4.3 List of Depths

  Given a binary tree, design an algorithm which creates a linked
  list of all the nodes at each depth (e.g. if you have a tree with
  depth D, you'll have D linked lists).

"""

def create_list_by_depth_recursive(root, lists=[], level=0):
  # DFS, recursive
  if root is None:
    return

  linked_list = None
  if len(lists) == level:
    linked_list = LinkedList()
    lists.append(linked_list)
  else:
    linked_list = lists[level]

  linked_list.add(root.value)
  create_list_by_depth_recursive(root.left, lists, level + 1)
  create_list_by_depth_recursive(root.right, lists, level + 1)
  
def create_list_by_depth_bfs(root):
  # BFS
  queue = deque()
  queue.append((root, 0))
  levels = {}
  while queue:
    node, level = queue.popleft()
    if level not in levels:
      # no linked list yet
      levels[level] = LinkedList()
    levels[level].add(node.value)
    if node.left:
      queue.append((node.left, level + 1))
    if node.right:
      queue.append((node.right, level + 1))
  return levels


class Test(unittest.TestCase):
  test_functions = [
    create_list_by_depth_recursive,
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

    lists = []
    create_list_by_depth_recursive(root, lists, 0)
    print("DFS")
    for level in lists:
      print(level.values())

    levels = create_list_by_depth_bfs(root)
    print("BFS")
    for key in levels:
      print(levels[key].values())

    
       
if __name__ == "__main__":
  unittest.main()