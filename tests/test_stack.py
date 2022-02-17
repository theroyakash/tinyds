import unittest
from tinyds import Stack


class StackTests(unittest.TestCase):

	def setUp(self):
		self.iterable: list[int] = [7, 14, 9, 8, 3, 2, 6, 4, 1, 5, 10, 11, 13, 12]
		self.stk = Stack(self.iterable[::-1])

	def test_stack_tos_and_insertion(self):
		self.stk.push(2000)
		self.assertEqual(2000, self.stk.tos())  # add assertion here

	def test_stack_pop(self):
		self.assertEqual(7, self.stk.pop())
		self.assertEqual(14, self.stk.pop())
		self.assertEqual(9, self.stk.pop())
		self.assertEqual(8, self.stk.pop())
		self.assertEqual(3, self.stk.pop())
		self.assertEqual(2, self.stk.pop())

	def test_stack_end(self):
		self.assertEqual(12, self.stk.end.value)


if __name__ == '__main__':
	unittest.main()
