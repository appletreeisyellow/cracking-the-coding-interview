class Stack:
  def __init__(self):
    self.items = []

  def is_empty(self):
    return len(self.items) == 0

  def pop(self):
    if self.items:
      return self.items.pop()
    return None

  def push(self, value):
    self.items.append(value)

  def peek(self):
    if self.items:
      return self.items[-1]
    return None

  def __len__(self):
    return len(self.items)