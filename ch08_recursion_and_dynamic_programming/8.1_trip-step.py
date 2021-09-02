"""

8.1 Triple Step

  A child is running up a staircase with n steps and can hop
  either 1 step, 2 steps, or 3 steps at a time. Implement a
  method to count how many possible ways the child can run up
  the stairs.

"""

def triple_step(n):
  if n < 0:
    return 0
  if n == 0:
    return 1
  if n == 1:
    return 1
  return triple_step(n - 1) + triple_step(n - 2) + triple_step(n - 3)


def triple_step_2(n):
  memo = [-1] * (n + 1)
  return  triple_step_recursion(n, memo)

def triple_step_recursion(n, memo):
  if n < 0:
    return 0
  # n = 0
  memo[0] = 1
  if n >= 1:
    memo[1] = 1
  if n >= 2:
    memo[2] = memo[1] + memo[0]
  if n > 2:
    for i in range(3, n + 1):
      memo[i] = memo[i - 1] + memo[i - 2] + memo[i - 3]
  return memo[n]

def test_triple_step():
  test_cases = [
    (-3, 0),
    (0, 1),
    (1, 1),
    (2, 2),
    (3, 4),
    (4, 7),
    (5, 13),
    (6, 24),
    (7, 44),
  ]

  test_functions = [
    triple_step,
    triple_step_2,
  ]

  for test_func in test_functions:
    for n, expected in test_cases:
      try:
        result = test_func(n)
        assert (result == expected), "Failed"
      except AssertionError as e:
        e.args += (test_func.__name__, n, "steps should take " \
          + str(expected) + " but got " + str(result))
        raise


if __name__ == "__main__":
  test_triple_step()