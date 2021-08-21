import unittest
from linked_list import LinkedList, LinkedListNode

"""

2.5 Sum Lists

  You have two numbers represented by a linked list, where each node
  contains a single digit. The digits are stored in reverse order,
  such that the 1's digit is at the head of the list. Write a function
  that adds the two numbers and returns the sum as a linked list.

  EXAMPLE
  
  Input: (7-> 1-> 6) + (5-> 9-> 2). That is, 617 + 295.
  Output: 2 -> 1 -> 9. That is 912

  FOLLOW UP

  Input: (6-> 1-> 7) + (2-> 9-> 5). That is, 617 + 295.
  Output: 9 -> 1-> 2. That is, 912

"""

def sum_lists(ll1, ll2):
  if (ll1 is None and ll2 is None):
    return None

  current1 = ll1.head
  current2 = ll2.head
  result = LinkedList()
  carry_over = 0

  # add overlapped digits
  while current1 is not None and current2 is not None:
    tmp_sum = current1.value + current2.value + carry_over
    if tmp_sum >= 10:
      carry_over = 1
    else:
      carry_over = 0
    result.add(tmp_sum % 10)
    current1 = current1.next
    current2 = current2.next

  # if there are more digits in the list,
  # append the rest the digit in ll1 or ll2 to the result
  if current1 is not None:
    while current1:
      tmp_sum = current1.value + carry_over
      if tmp_sum >= 10:
        carry_over = 1
      else:
        carry_over = 0
      result.add(tmp_sum % 10)
      current1 = current1.next

  if current2 is not None:
    while current2:
      tmp_sum = current2.value + carry_over
      if tmp_sum >= 10:
        carry_over = 1
      else:
        carry_over = 0
      result.add(tmp_sum % 10)
      current2 = current2.next

  # append carry_over if necessary
  if carry_over > 0:
    result.add(carry_over)

  return result

def sum_lists_recursive(ll1, ll2):
  if ll1 is None and ll2 is None:
    return None

  return add_node(None if ll1 is None else ll1.head,
                  None if ll2 is None else ll2.head,
                  0)

def add_node(n1, n2, carry_over):
  if (n1 is None and n2 is None and carry_over == 0):
    return None

  result = LinkedList()
  value = carry_over
  if n1 is not None:
    value += n1.value

  if n2 is not None:
    value += n2.value

  result.add(value % 10)

  if n1 is not None or n2 is not None:
    more = add_node(None if n1 is None else n1.next,
                    None if n2 is None else n2.next,
                    1 if value >= 10 else 0)
    if more is not None:
      result.tail.next = more.head
      result.tail = result.tail.next
  
  return result

class Test(unittest.TestCase):
  test_cases = [
    # add test cases here, ("test-case", True)
    ([7, 1, 6], [5, 9, 2], [2, 1, 9]),
    ([5, 2], [7], [2, 3]),
    ([5], [8], [3, 1]),
    ([7, 9], [3, 2], [0, 2, 1]),
    ([8, 9], [9], [7, 0, 1])
  ]
  test_functions = [
    # add testing functions here
    sum_lists,
    sum_lists_recursive,
  ]

  def test(self):
    for values1, values2, expected in self.test_cases:
      for test_func in self.test_functions:
        try:
          expected = expected.copy()
          result = test_func(LinkedList(values1), LinkedList(values2))
          assert (result.values() == expected), "Failed!"
        except AssertionError as e:
          e.args += (test_func.__name__, values1, values2, "should be " + str(expected))
          raise


if __name__ == "__main__":
  unittest.main()