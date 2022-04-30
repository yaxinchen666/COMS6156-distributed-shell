import unittest
import random
from calculator import sum_list


def rand_list(size):
  return [random.random() for i in range(size)]


class TestSum(unittest.TestCase):

  def test_sum(self):
    length = 100000
    for i in range(10):
      l1 = rand_list(length)
      l2 = rand_list(length)
      result = sum_list(l1, l2)
      for i in range(len(result)):
        self.assertEqual(result[i], l1[i] + l2[i],
                         "{} + {} should be {} but get {}".format(l1[i], l2[i], l1[i] + l2[i], result[i]))


if __name__ == '__main__':
  unittest.main()
