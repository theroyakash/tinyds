import unittest
from tinyalgo import binary_search


class BinarySearch(unittest.TestCase):
	def test_bs_int(self):
		iterable: list[int] = [1, 2, 3, 4, 5, 61]
		self.assertEqual(0, binary_search(iterable, 1))  # add assertion here

	def test_bs_float(self):
		iterable: list[float] = [1.3, 13.0, 35.7, 124.0]
		self.assertEqual(2, binary_search(iterable, 35.7))

	def test_notinbs(self):
		iterable: list[float] = [1.3, 13.0, 35.7, 124.0]
		self.assertEqual(-1, binary_search(iterable, 35.123))


if __name__ == '__main__':
	unittest.main()
