import unittest
from linked_list import LinkedList

"""

2.4 Partition
  
  Write code to partition a linked list around a value x, such that
  all nodes less than x come before all nodes greater than or equal
  to x. If x is contained within the list, the values of x only need
  to be after the elements less than x (see below). The partition
  element x can appear anywhere in the "right partition"; it does not
  need to appear between the left and right partitions.

  EXAMPLE
  Input:  3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition = 5]
  Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8

"""

def partition(ll, x):
  current = ll.tail = ll.head
  
  while current is not None:
    next_node = current.next
    current.next = None
    if current.value < x:
      # put at head
      current.next = ll.head
      ll.head = current
    else:
      # put at tail
      ll.tail.next = current
      ll.tail = current
    current = next_node

  if ll.tail.next is not None:
    ll.tail.next = None
  
  return ll.head


class Test(unittest.TestCase):
  ll = LinkedList([3, 5, 8, 5, 10, 2, 1])
  print(ll)
  partition(ll, 5)
  print(ll)
  partition(ll, 8)
  print(ll)


if __name__ == "__main__":
  unittest.main()