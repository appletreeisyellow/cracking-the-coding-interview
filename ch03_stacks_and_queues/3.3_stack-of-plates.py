from stack import Stack

"""

3.3 Stack of Plates

  Imagine a (literal) stack of plates. If the stack gets too high, it
  might topple. Therefore, in real life, we would likely start a new
  stack when the previous stack exceeds some threshold. Implement a
  data structure SetOfStacks that mimics this. SetOfStacks should be
  composed of several stacks and should create a new stack once the
  previous one exceeds capacity. SetOfStacks.push() and SetOfStacks.pop()
  should behave identically to a single stack (that is, pop() should 
  return the same values as it would if there were just a single stack).

  FOLLOW UP

  Implement a function popAt(int index) which performs a pop operation
  on a specific substack.

"""

class SetOfStacks():
  def __init__(self, threshold):
    self.threshold = threshold
    self.set_of_stacks = []
    self.length = 0

  def is_empty(self):
    return self.length == 0

  def push(self, value):
    # determine if a new stack should be created or not
    if self.length % self.threshold == 0:
      newstack = Stack()
      newstack.push(value)
      self.set_of_stacks.append(newstack)
    else:
      top_index = self._current_set_idx()
      self.set_of_stacks[top_index].push(value)
    self.length += 1

  def pop(self):
    top_index = self._current_set_idx()
    value = self.set_of_stacks[top_index].pop()
    self.length -= 1
    # remove the empty Stack if necessary
    if self.set_of_stacks[top_index].is_empty():
      self.set_of_stacks.pop()
    return value

  def peek(self):
    top_index = self._current_set_idx()
    return self.set_of_stacks[top_index].peek()

  def __len__(self):
    return self.length

  def _current_set_idx(self):
    # return the current index of the top set
    return (self.length - 1) // self.threshold

  # TODO: follow up question
  def pop_at(self, index):
    # check if the index exist
    if index > self._current_set_idx():
      return None

    # pop the value

    # decrease the length

    # return the value

def test_set_of_stacks():
  s = SetOfStacks(threshold=2)
  assert s.is_empty() == True

  s.push(3)
  assert s.peek() == 3

  s.push(5)
  assert s.peek() == 5

  s.push(6)
  assert len(s) == 3
  assert s.peek() == 6

  print("passed")

if __name__ == "__main__":
  test_set_of_stacks()
