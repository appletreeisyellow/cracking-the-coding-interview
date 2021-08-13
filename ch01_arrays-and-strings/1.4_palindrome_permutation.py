import unittest

def is_palindrome_permutation(string):
  # a palindrome is a string has at most one character that is odd
  
  # assume case-insensitive, space doesn't count
  
  # have a Hath table to store if each char appeared as 
  # odd times or even times
  # key is character
  # value is the number of times the letter appeared
  string = string.lower()
  char_set = {}
  count_odd = 0
  for c in string:
    val = char_value(c)
    if val != -1: # only put the letters into hash table
      if c not in char_set:
        char_set[c] = 1
      else:
        char_set[c] += 1
      if char_set[c] % 2: # is odd
        count_odd += 1
      else:
        count_odd -= 1
  return count_odd <= 1

def char_value(c):
  a = ord("a")
  z = ord("z")
  upper_a = ord("A")
  upper_z = ord("Z")
  val = ord(c)

  if a <= val <= z:
    return val - a
  if upper_a <= val <= upper_z:
    return val - upper_a
  return -1 # non-letter


class Test(unittest.TestCase):
  test_cases = [
    ("a", True),
    ("bb", True),
    ("abba", True),
    ("abbs", False),
    ("caabaac", True),
    ("Tact Coa", True),
    ("Tact Poa", False),
    ("tactcoapapa", True),
    ("a-bba", True),
    ("a-bcba", True),
  ]
  test_functions = [
    # add testing functions here
    is_palindrome_permutation,
  ]

  def test(self):
    for text, expected in self.test_cases:
      for test_func in self.test_functions:
        try:
          assert (test_func(text) == expected), "Failed!"
        except AssertionError as e:
          e.args += (test_func.__name__, text)
          raise


if __name__ == "__main__":
  unittest.main()