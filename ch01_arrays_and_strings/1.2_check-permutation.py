import unittest

"""

1.2 Check Permutation

  Given two strings, write a method to decide if one is
  a permutation of the other.
  
"""

# assume using ASCII 8-bit
# assume case sensitive & space is significant
# "god   " is different from "dog"

def check_permutation_by_sort(str1, str2):
  if len(str1) != len(str2):
    return False
  # sort the string and compare
  s1 = sorted(str1)
  s2 = sorted(str2)
  for i in range(len(s1)):
    if s1[i] != s2 [i]:
      return False;
  return True

def check_permutation_by_count(str1, str2):
  if len(str1) != len(str2):
    return False
  # count the number of times each char appear
  # then compare the number for str1 and str2
  counter = [0] * 256
  for c in str1:
    counter[ord(c)] += 1
  # de-counting the char in str2
  for c in str2:
    if counter[ord(c)] == 0:
      return False
    counter[ord(c)] -= 1
  return True


class Test(unittest.TestCase):
  test_cases = [
    # add test cases here, ("test-case", True)
    ("dog", "god", True),
    ("1235", "1532", True),
    ("dog  ", "god", False),
    ("dog", "God", False),
  ]
  test_functions = [
    # add testing functions here
    check_permutation_by_sort,
  ]

  def test(self):
    for str1, str2, expected in self.test_cases:
      for test_func in self.test_functions:
        assert (
          test_func(str1, str2) == expected
        ), "{test_func.__name__} failed for value: {text}"


if __name__ == "__main__":
  unittest.main()