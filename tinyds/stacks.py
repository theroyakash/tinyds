"""
Stacks most optimized implementation with Linked Lists
"""
from typing import Any, Union, Optional
from dataclasses import dataclass


@dataclass(order=True)  # Sets the Node objects hashable and comparable
class Node:
	value: Any
	following: Optional["Node"] = None


class Stack:
	def __init__(self, nodes: Union[list[Node], None] = None) -> None:
		"""
		Initialize a stack with no node or with a list of nodes.
		Args:
			- nodes: To initialize a empty stack pass nothing, else pass a list of nodes.
		"""
		self.head: Node = None
		self.end: Node = None

		if nodes:
			for node in nodes:
				self.push(node)

	def push(self, value: Any) -> None:
		"""
		Push element to the stack.
		Args:
			value: Push Any value onto the stack.
		"""
		
		newNode = Node(value, following = None)

		if self.head is None:
			self.head = newNode
			self.end = newNode
		else:
			temp = self.head
			self.head = newNode
			self.head.following = temp

	def tos(self) -> Any:
		"""
		Get the top of the stack with out removing it. O(1) Operation.
		"""
		return self.head.value

	def pop(self) -> Optional[Node]:
		if self.head is None:
			return None
		else:
			temp = self.head
			self.head = self.head.following

		return temp.value


	def __repr__(self) -> str:
		stack = []
		head = self.head

		while head is not None:
			stack.append(head.value)
			head = head.following

		return f"{stack}"


if __name__ == '__main__':
	"""
	For testing purposes + More code for testing in the test folder/
	"""
	
	from rich.console import Console
	console = Console()
	import random

	elem = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
	random.shuffle(elem)

	stk = Stack(elem)
	console.print(stk)

	stk.push(2000)
	stk.push(3000)
	stk.push(4000)
	stk.push(5000)
	console.print(stk)

	for _ in range(5):
		print("Popping", stk.pop())

	console.print("End at", stk.end)
	console.print("stack now:", stk)