import unittest

def string_compression(string):
  # use one var to count the current letter
  cur_char = ""
  count = 0
  compressed = [] # key! not using "" but [] to avoid long string run time
  for c in string:
    if c != cur_char:
      if cur_char != "": # non-first letter
        compressed.append(cur_char + str(count))
      cur_char = c
      count = 1
    else:
      count += 1
  # put the last letter in the compression
  compressed.append(cur_char + str(count))

  # if the compressed string is not smaller
  # return the origin string
  return min(string, "".join(compressed), key=len)

class Test(unittest.TestCase):
  test_cases = [
    # add test cases here, ("test-case", True)
    # no change
    ("a", "a"),
    ("aa", "aa"),
    ("aA", "aA"),
    ("aab", "aab"),
    # shorter after compression
    ("aaa", "a3"),
    ("aabcccccaaa", "a2b1c5a3"),
    ("aabCCcccaaa", "a2b1C2c3a3"),
  ]
  test_functions = [
    # add testing functions here
    string_compression,
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