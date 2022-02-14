"""
Most optimized code for Binary Search.
Try to approach binary search problems with iterative fashion because this
works with the array in-place so no extra space is required. No recursion
error will be there if the problem is too big to handle.
"""
from typing import Union

T = Union[int, float]


def binary_search(array: list[T], target: T) -> T:
	"""
	Binary Search Iterative Algorithm
	Args:
		array: Array of Integers or Float is expected
		target: Integers or Float

	Returns:
		position of the target value or -1 if not found.
	"""
	start: int = 0
	end: int = len(array) - 1
	middle: int = 0

	while start < end:
		# Set the middle for every step of the while loop
		middle = (start + end) // 2

		if array[middle] < target:
			# Go to the right part of the array
			# Update the start to mid + 1 and end remains the same
			start = middle + 1
		elif array[middle] > target:
			# This means we over-shoot the value should be in the left sub-array
			# So set the end to mid - 1
			end = middle - 1
		elif array[middle] == target:
			return middle

	return -1


if __name__ == "__main__":
	print(binary_search(array=[1, 2, 3, 5], target=6))
	print(binary_search(array=[1, 2, 3, 5, 8], target=2))
