from tinyds import bimap
import unittest


class BiMapSearch(unittest.TestCase):
	def test_bs_int(self):
		bi_map = bimap.BiMap()
		bi_map.put({
			"1": "2",
			"theroyakash": "hola"
		})
		self.assertEqual("2", bi_map.get("1"))  # lookup check
		self.assertEqual("theroyakash", bi_map.get_reversed("hola"))  # reverse look up check


if __name__ == '__main__':
	unittest.main()
