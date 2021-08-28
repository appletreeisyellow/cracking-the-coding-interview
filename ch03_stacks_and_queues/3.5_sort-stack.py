import unittest
from stack import Stack

"""

3.5 Sort Stack

  Write a program to sort a stack such that the smallest items are
  on the top. You can use an additional temporary stack, but you
  may not copy the elements into any other data structure (such as
  an array). The stack supports the following operations: push, pop,
  peek, and isEmpty.

"""

class SortedStack(Stack):
  def __init__(self):
    super().__init__()
    self.temp_stack = Stack()

  # if the current popped value is greater than the top of the sorted value,
  # pop and put all the values in the sorted stack that is smaller than the
  # current value to the original stack, push the current value, put back
  # the sorted values
  def push(self, value):
    if self.is_empty() or value < self.peek():
      super().push(value)
    else:
      # pop the stack values unto temp_stack
      while not self.is_empty() and value > self.peek():
        self.temp_stack.push(self.pop())
      super().push(value)
      # pop the temp_stack back to stack
      while not self.temp_stack.is_empty():
        super().push(self.temp_stack.pop())


def convert_array_to_stack(array):
  s = Stack()
  for value in array:
    s.push(value)
  return s

class Test(unittest.TestCase):
  def test_push_one(self):
    s = SortedStack()
    s.push(1)
    assert len(s) == 1

  def test_push_two(self):
    s = SortedStack()
    s.push(1)
    s.push(2)
    assert len(s) == 2

  def test_push_three(self):
    s = SortedStack()
    s.push(1)
    s.push(2)
    s.push(3)
    assert len(s) == 3

  def test_pop_one(self):
    s = SortedStack()
    s.push(1)
    assert s.pop() == 1

  def test_pop_two(self):
    s = SortedStack()
    s.push(1)
    s.push(2)
    assert s.pop() == 1
    assert s.pop() == 2

  def test_pop_three(self):
    s = SortedStack()
    s.push(1)
    s.push(2)
    s.push(3)
    assert s.pop() == 1
    assert s.pop() == 2
    assert s.pop() == 3

  def test_push_mixed(self):
    s = SortedStack()
    s.push(1)
    s.push(2)
    s.push(4)
    s.push(3)
    s.push(5)
    assert s.pop() == 1
    assert s.pop() == 2
    assert s.pop() == 3
    assert s.pop() == 4
    assert s.pop() == 5
    

if __name__ == "__main__":
  unittest.main()