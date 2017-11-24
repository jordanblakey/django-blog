# PYTEST SAMPLE TESTS


def func(x):
  return x + 1

###########################################
# TESTS
###########################################

# Example of a failing test
# def test1():
#   assert func(3) == 5

# Example of a passing test


def test2():
  assert func(4) == 5  # basic assertion format


# content of test_class.py
class TestClass(object):

  def test_one(self):
    x = "this"
    assert 'h' in x

  def test_two(self):
    class Person:
      eyes = True

    x = Person()

    assert hasattr(x, 'eyes')
