import unittest

"""

1.9 String Rotation

  Assume you have a method is isSubstring which checks if one word
  is a substring of another. Given two strings, s1 and s2, write
  code to check if s2 is a rotation of s1 using only one call to isSubstring
  (e.g. "waterbottle" is a rotation of "erbottlewat").

"""

def is_string_rotation(s1, s2):
  if len(s1) != len(s2) or len(s1) == 0:
    return False

  # Regardless what the division point is,
  # if s2 is a substring of s1, s2 will always
  # be a substring of s1s1

  s1s1 = s1 + s1
  return isSubstring(s1s1, s2)

"""
 
 The runtime of this func depends on the runtime of isSubstring.
 But if assume is Substring runs in O(A+B) time (on strings of 
 length A and B), then the runtime of isRotation is O(N).

"""

class Test(unittest.TestCase):
  test_cases = [
    # add test cases here, ("test-case", True)
    ("abbbb", "bbabb", True),  
    ("waterbottle", "erbottlewat", True),
    ("testteart", "earttestt", True),
    ("", "", False),
    ("ab", "a", False),
    ("a", "ab", False),
  ]
  test_functions = [
    # add testing functions here
  ]

  def test(self):
    for text, expected in self.test_cases:
      for test_func in self.test_functions:
        try:
          assert (test_func(text) == expected), "Failed!"
        except AssertionError as e:
          e.args += (test_func.__name__, text, "should be " + str(expected))
          raise


if __name__ == "__main__":
  unittest.main()