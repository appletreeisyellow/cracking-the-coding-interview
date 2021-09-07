import unittest

"""

8.5 Recursive Multiply

  Write a recursive function to multiply two positive integers
  without using the * operator (or / operator). You can use addition,
  subtraction, and bit shifting, but you should minimize the number
  of those operations.

"""

def recursive_multiply(a, b):
  smaller = a if a < b else b
  bigger = a if a > b else b
  return recursive_multiply_helper(smaller, bigger)

def recursive_multiply_helper(smaller, bigger):
  if smaller == 0:
    return 0
  if smaller == 1:
    return bigger

  half = smaller >> 1 # divided by 2
  half_prod = recursive_multiply(half, bigger)
  if (smaller % 2 == 0):
    return half_prod + half_prod
  else:
    return half_prod + half_prod + bigger

class Test(unittest.TestCase):
  test_cases = [
    # add test cases here, ("test-case", True)
    ((2, 3), 6),
    ((9, 8), 72),
    ((5, 5), 25),
    ((0, 3), 0),
    ((1, 5), 5),
  ]
  test_functions = [
    # add testing functions here
    recursive_multiply,
  ]

  def test(self):
    for test_func in self.test_functions:
      for values, expected in self.test_cases:
        try:
          result = test_func(values[0], values[1])
          assert (result == expected), "Failed!"
        except AssertionError as e:
          e.args += (test_func.__name__, values, "should be " + \
            str(expected) + ", but got " + str(result))
          raise


if __name__ == "__main__":
  unittest.main()