class Node:
  def __init__(self, value):
    self.value = value
    self.parent = None
    self.left = None
    self.right = None

class BinarySearchTree:
  def __init__(self):
    self.root = None

  def insert(self, value):
    new = Node(value)
    if self.root is None:
      self.root = new
      return

    current = self.root
    while current:
      if value <= current.value:
        if current.left:
          current = current.left
        else:
          current.left = new
          new.parent = current
          return
      else: # value > current.value
        if current.right:
          current = current.right
        else:
          current.right = new
          new.parent = current
          return

  def get_node(self, value):
    current = self.root
    while current:
      if value == current.value:
        return current
      if value <= current.value:
        current = current.left
      else:
        current = current.right
    raise Exception("No such value in the tree")


if __name__ == "__main__":
  bst = BinarySearchTree()
  bst.insert(20)
  bst.insert(9)
  bst.insert(5)
  bst.insert(31)
  bst.insert(1)
  bst.insert(3)
