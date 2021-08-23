from stack import Stack

class StackWithMin(Stack):
  def __init__(self):
    super().__init__()
    self.minvals = Stack()

  def push(self, value):
    super().push(value)
    if not self.minvals or value <= self.get_min():
      self.minvals.push(value)

  def pop(self):
    len(self.minvals)
    value = super().pop()
    if value == self.get_min():
      self.minvals.pop()
    return value

  def get_min(self):
    if self.minvals.is_empty():
      return None
    return self.minvals.peek()

def test_min_stack():
  newstack = StackWithMin()
  assert newstack.get_min() is None

  newstack.push(5)
  assert newstack.get_min() == 5

  newstack.push(6)
  assert newstack.get_min() == 5

  newstack.push(3)
  assert newstack.get_min() == 3

  newstack.push(7)
  assert newstack.get_min() == 3

  newstack.push(3)
  assert newstack.get_min() == 3

  newstack.pop()
  assert newstack.get_min() == 3

  newstack.pop()
  assert newstack.get_min() == 3


  print("passed")

if __name__ == "__main__":
  test_min_stack()

