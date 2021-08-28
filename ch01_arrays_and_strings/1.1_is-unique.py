import unittest

"""

1.1 Is Unique

  Implement an algorithm to determine if a string has
  all unique characters. What if you cannot use additional
  data structures?
  
"""

# time O(n), space O(1)
def is_unique(str):
  # assume the characters are ASCII string -> 128 char
  if (len(str) > 128):
    return False

  charTable = {}

  # if any character has appeared once, return false
  # each char corresponding to a slot in charTable
  for c in str:
    if c in charTable:
      return False
    charTable[c] = True
  return True

def is_unique_set(str):  
  return len(set(str)) == len(str)

class Test(unittest.TestCase):
  test_cases = [
    ("", True),
    ("abcd", True),
    ("adsfewr4", True),
    ("asdfewras", False),
    ("sdf adsfe ()", False),
    ("".join([chr(val) for val in range(128)]), True), # unique 128 chars
    ("".join([chr(val // 2) for val in range(129)]), False), # non-unique 129 chars
  ]
  test_functions = [
    is_unique,
    is_unique_set,
  ]

  def test(self):
    for text, expected in self.test_cases:
      for test_func in self.test_functions:
        assert (
          test_func(text) == expected
        ), "{test_func.__name__} failed for value: {text}"


if __name__ == "__main__":
  unittest.main()