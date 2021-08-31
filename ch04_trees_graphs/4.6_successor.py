import unittest
from collections import deque
from binary_tree import BinaryNode
from binary_search_tree import BinarySearchTree


"""

4.6 Successor

  Write an algorithm to find the "next" node (i.e., in-order successor)
  of a given node in a binary search tree. You may assume that each
  node has a link to its parent.

"""
def successor(node):
  # if the node has right node, find the min of right node
  # else, find the smallest parent
  if node is None:
    return None

  if node.right:
    return get_min_node(node.right)

  current = node.parent
  while current:
    if current.value > node.value:
      return current
    current = current.parent
  return current


def get_min_node(node):
  if node is None:
    return node
  current = node
  while current:
    if current.left:
      current = current.left
    return current

def _gen_test_tree():
  """
  BST
           10
      3          20
   2     6    13    25
  1    5       15     27
  """
  bst = BinarySearchTree()
  bst.insert(10)
  bst.insert(3)
  bst.insert(20)
  bst.insert(2)
  bst.insert(6)
  bst.insert(13)
  bst.insert(25)
  bst.insert(1)
  bst.insert(5)
  bst.insert(15)
  bst.insert(27)
  return bst

def test():
  bst = _gen_test_tree()
  inputs = [1, 2, 3, 5, 6, 10, 13, 15, 20, 25, 27]
  outputs = inputs[1:]
  outputs.append(None)


  for x, y in zip(inputs, outputs):
    test = bst.get_node(x)
    succ = successor(test)
    if succ is not None:
      try:
        assert succ.value == y, "Failed"
      except AssertionError as e:
        e.args += ("test value", str(test.value), "should be " + str(y) \
          + " but actually got " + str(succ.value))
        raise
    else:
      assert succ is None

if __name__ == "__main__":
  test()