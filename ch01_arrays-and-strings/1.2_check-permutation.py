import unittest


class Test(unittest.TestCase):
  test_cases = [
    # add test cases here, ("test-case", True)
  ]
  test_functions = [
    # add testing functions here
  ]

  def test(self):
    for text, expected in self.test_cases:
      for test_func in self.test_functions:
        assert (
          test_func(text) == expected
        ), "{test_func.__name__} failed for value: {text}"


if __name__ == "__main__":
  unittest.main()