import unittest

"""

1.5 One Away

  There are three types of edits that can be performed on
  strings: insert a character, remove a character, or
  replace a character. Given two strings, write a function
  to check if they are one edit (or zero edits) away.

  EXAMPLE
  pale, ple   -> true
  pales, pale -> true
  pale, bale  -> true
  pale, bae   -> false

"""

def is_one_away(str1, str2):
  len1 = len(str1)
  len2 = len(str2)
  if len1 == len2:
    return is_one_char_replaceable(str1, str2)
  elif len1 + 1 == len2:
    return is_one_char_insertable(str1, str2)
  elif len2 + 1 == len1:
    return is_one_char_insertable(str2, str1)
  else:
    return False

def is_one_char_replaceable(str1, str2):
  found_diff = False
  for c1, c2 in zip(str1, str2):
    if c1 != c2:
      if found_diff:
        return False
      found_diff = True
  return True

def is_one_char_insertable(str1, str2):
  # assume length of str1 < str2
  index1 = 0
  index2 = 0
  found_diff = False
  while index1 < len(str1) and index2 < len(str2):
    if str1[index1] != str2[index2]:
      if found_diff:
        return False
      found_diff = True
      index2 += 1
    else:
      index1 += 1
      index2 += 1
  return True

class Test(unittest.TestCase):
  test_cases = [
    # add test cases here, ("test-case", True)
    ("pale", "ple", True),
    ("pales" ,"pale", True),
    ("pale" ,"pales", True),
    ("pale", "bale", True),
    ("pale", "bae", False),
    ("pale", "palesd", False),
    ("pale", "btle", False),
  ]
  test_functions = [
    # add testing functions here
    is_one_away,
  ]

  def test(self):
    for text1, text2, expected in self.test_cases:
      for test_func in self.test_functions:
        try:
          assert (test_func(text1, text2) == expected), "Failed!"
        except AssertionError as e:
          e.args += (test_func.__name__, text1, text2, "should be " + str(expected))
          raise


if __name__ == "__main__":
  unittest.main()