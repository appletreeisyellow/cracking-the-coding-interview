"""

4.2 Minimal Tree

  Given a sorted (increasing order) array with unique integer
  elements, write an algorithm to create a binary search tree
  with minimal height.

"""

class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

def construct_minimal_tree(array):
  if len(array) == 0:
    return None

  if len(array) == 1:
    return Node(array[0])

  # insert the middle element
  middle_index = len(array) // 2
  tree = Node(array[middle_index])

  # insert the left subtree
  tree.left = construct_minimal_tree(array[:middle_index])

  # insert the right subtree
  tree.right = construct_minimal_tree(array[(middle_index+1):])

  return tree

def print_tree(root):
  if root is None:
    return

  print_tree(root.left)
  print(root.value)
  print_tree(root.right)

def test_construct_minimal_tree():
  test_cases = [
    [],
    [1],
    [1, 2],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
  ]

  for test in test_cases:
    tree = construct_minimal_tree(test)
    print("test " + str(test))
    print_tree(tree)

if __name__ == "__main__":
  test_construct_minimal_tree()