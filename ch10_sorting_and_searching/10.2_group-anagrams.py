import unittest

"""

10.2 Group Anagrams

  Write a method to sort an array of strings so that all the
  anagrams are next to each other.

"""

def group_anagrams(array):
  hash_string = {} # "abc": ["bac", 'bca', "abc"]
  for string in array:
    key = sort_string(string)
    if key not in hash_string:
      hash_string[key] = []
    hash_string[key].append(string)

  index = 0
  for key in hash_string:
    for string in hash_string[key]:
      array[index] = string
      index += 1
  return array

def sort_string(string):
  string_array = list(string)
  string_array.sort()
  sorted_str = "".join(string_array)
  return sorted_str


class Test(unittest.TestCase):
  test_cases = [
    # add test cases here, ("test-case", True)
    (["add", "ab", "dda", "ba"]),
    (["cc", "a", "cc", "dd"]),
  ]
  test_functions = [
    # add testing functions here
    group_anagrams,
  ]

  def test(self):
    for test_func in self.test_functions:
      for values in self.test_cases:
        try:
          result = test_func(values)
          print(result)
        except AssertionError as e:
          e.args += (test_func.__name__, values)
          raise


if __name__ == "__main__":
  unittest.main()