import unittest

"""

1.3 URLify

  Write a method to replace all spaces in a string with
  "%20". You may assume that the string has sufficient
  space at the end to hold the additional characters, and
  that you are given the "true" length of the string.
  (Note: if implementing in Java, please use a character
  array so that you can perform this operation in place.)

  EXAMPLE
  Input:  "Mr John Smith    ", 13
  Output: "Mr%20John%20Smith"

"""

def urlify(string, trueLength):
  spaceNum = 0
  for i in range(0, trueLength):
    if (string[i] == " "):
      spaceNum += 1
  index = trueLength + spaceNum * 2
  newStringArr = [" "] * index
  for i in range(trueLength-1, -1, -1):
    if (string[i] == " "):
      newStringArr[index-1] = "0"
      newStringArr[index-2] = "2"
      newStringArr[index-3] = "%"
      index -= 3
    else:
      newStringArr[index-1] = string[i]
      index -= 1
  
  newString = "".join([str(c) for c in newStringArr])
  return newString

class Test(unittest.TestCase):
  test_cases = [
    # add test cases here, ("test-case", True)
    ("Mr John Smith    ", 13, "Mr%20John%20Smith"),
    ("Hello  World    ", 12, "Hello%20%20World"),
    (" Hello  World      ", 13, "%20Hello%20%20World"),
  ]
  test_functions = [
    # add testing functions here
    urlify,
  ]

  def test(self):
    for text, length, expected in self.test_cases:
      for test_func in self.test_functions:
        assert (
          test_func(text, length) == expected
        )


if __name__ == "__main__":
  unittest.main()