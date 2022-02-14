from typing import Any


class BiMap:
	"""
	Bi-directional HashMap that hashes both way. Find key as well as values with O(1) time.
	Criteria:
		- The values must not be same for every key.
		- Both the key as well as values have to be same.
	"""
	def __init__(self):
		self.default: dict[Any, Any] = {}
		self.reverseLookup: dict[Any, Any] = {}

	def put(self, pair: dict[Any, Any]):
		"""
		Put key-pair values into the BiMap
		Args:
			pair: A dictionary that has more than one key-value pairs. We put all into the BiMap
		"""
		for key in pair:
			self.default[key] = pair[key]
			self.reverseLookup[pair[key]] = key

	def get_default(self) -> dict[Any, Any]:
		"""
		Get the representation of the default key-value pair
		Returns:
			The default key value pairs
		"""
		return self.default

	def get_reversed_table(self) -> dict[Any, Any]:
		"""
		Get the representation of the reverse value-key pair
		Returns:
			The reverse value-key pair.
		"""
		return self.reverseLookup

	def get(self, key: Any) -> Any:
		return self.default[key]

	def get_reversed(self, value: Any) -> Any:
		return self.reverseLookup[value]
