from typing import Union

T = Union[int, float]


def binary_search(iterable: list[T], search_key: T) -> int:
	"""
	Binary Search Implementation [TinyDS]
	Args:
		iterable: sorted iterable list of int or float
		search_key: Searching Item of type int or float

	Returns:
		Index of element if found else `FALSE`
	"""

	mid: int = len(iterable) // 2

	if iterable[mid] == search_key:
		return mid

	if search_key < iterable[mid]:
		return binary_search(iterable[:mid], search_key)
	else:
		return binary_search(iterable[mid+1:], search_key)

	return False
