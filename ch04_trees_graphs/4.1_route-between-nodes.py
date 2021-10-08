import unittest
from collections import deque

"""

4.1 Route Between Nodes

  Given a directed graph, design an algorithm to find out whether
  there is a route between two nodes.
  
"""

"""
A - B
|   |
C - D - E - F
    |   |
    G - H
        |
        I - J - K
        | 
        L 

O - P
|  /
Q
"""

def has_route_dfs_recursion(graph, start, end, visited=None):
  if visited is None:
    visited = set()

  for node in graph[start]:
    if node not in visited:
      visited.add(node)
      if node == end or has_route_dfs_recursion(graph, node, end, visited):
        return True
  return False


def has_route_dfs_stack(graph, start, end):
  if start == end:
    return True
  visited = set()
  stack = deque()
  stack.append(start)
  visited.add(start)
  while stack:
    node = stack.pop()
    for next_node in graph[node]:
      if next_node not in visited:
        if next_node == end:
          return True
        else:
          stack.append(next_node)
          visited.add(next_node)
  return False


def has_route_bfs(graph, start, end):
  if start == end:
    return True
  visited = set()
  queue = deque()
  queue.append(start)
  visited.add(start)
  while queue:
    node = queue.popleft()
    for adjacent in graph[node]:
      if adjacent not in visited:
        if adjacent == end:
          return True
        else:
          queue.append(adjacent)
          visited.add(adjacent)
  return False


class Test(unittest.TestCase):
  graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D"],
    "D": ["C", "E", "G"],
    "E": ["D", "F", "H"],
    "F": ["E"],
    "G": ["H"],
    "H": ["I"],
    "I": ["J", "L"],
    "J": ["I", "K"],
    "K": ["J"],
    "L": ["I"],
  }

  tests = [
    ("A", "L", True),
    ("A", "B", True),
    ("E", "K", True),
    ("F", "K", True),
    ("K", "I", True),
    ("L", "H", False),
    ("H", "A", False),
    ("G", "C", False),
  ]

  def test_has_route_dfs(self):
    for (start, end, expected) in self.tests:
      assert has_route_dfs_recursion(self.graph, start, end) == expected
      assert has_route_dfs_stack(self.graph, start, end) == expected

  def test_has_route_bfs(self):
    for (start, end, expected) in self.tests:  
      assert has_route_bfs(self.graph, start, end) == expected
    
      


if __name__ == "__main__":
  unittest.main()