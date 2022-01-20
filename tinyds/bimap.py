from typing import Any


class BiMap:
	"""
	Bi-directional HashMap that hashes both way. Find key as well as values with O(1) time
	"""
	def __init__(self):
		self.default: dict = {}
		self.reverseLookup: dict = {}

	def put(self, pair: dict):
		for key in pair:
			self.default[key] = pair[key]
			self.reverseLookup[pair[key]] = key

	def get(self, key: Any) -> Any:
		return self.default[key]

	def get_reversed(self, value: Any) -> Any:
		return self.reverseLookup[value]
