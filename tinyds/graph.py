"""
Graph, most simple implementation. For more rigorous implementation
see AKDSFramework at docs.akdsframework.iamroyakash.com
"""

from typing import Any


# Undirected unweighted graph
class Graph:
	def __init__(self, nodes: int, edges: list[tuple[int, int]]):
		"""
		Undirected unweighted Graph class
		Args:
			nodes: (int) number of nodes in the graph
			edges: (tuple of int, int) indicating edges between two node number
		"""
		self.values = [[] for _ in range(0, nodes)]

		for u, v in edges:
			self.values[u].append(v)
			self.values[v].append(u)

	def __repr__(self):
		return "\n".join([f"{i}: {neighbors}" for i, neighbors in enumerate(self.values)])

	def __str__(self):
		return repr(self)

