import unittest
from stack import Stack

"""

3.4 Queue via Stacks

  Implement a MyQueue class which implements a queue using two stacks.

"""

class MyQueue:
  def __init__(self):
    self.new_stack = Stack()
    self.old_stack = Stack()

  def _shift_stacks(self):
    # put all the value from new to old
    if self.old_stack.is_empty():
      while not self.new_stack.is_empty():
        new_value = self.new_stack.pop()
        self.old_stack.push(new_value)

  def enqueue(self, value):
    self.new_stack.push(value)

  def dequeue(self):
    if self.is_empty():
      return None
    
    self._shift_stacks()
    return self.old_stack.pop()

  def peek(self):
    if self.is_empty():
      return None

    self._shift_stacks()
    return self.old_stack.peek()

  def __len__(self):
    return len(self.old_stack) + len(self.new_stack)

  def is_empty(self):
    return len(self) == 0


def test_queue():
  queue = MyQueue()
  assert queue.is_empty() == True

  # test enqueue and peek
  queue.enqueue(3)
  assert queue.peek() == 3

  queue.enqueue(5)
  assert queue.peek() == 3

  queue.enqueue(4)
  assert queue.peek() == 3

  # test dequeue and length
  assert queue.dequeue() == 3
  assert len(queue) == 2
  assert queue.dequeue() == 5
  assert len(queue) == 1

  print("passed")

if __name__ == "__main__":
  test_queue()