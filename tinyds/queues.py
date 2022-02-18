"""
Queues most optimized implementation with Linked Lists
"""
from typing import Any, Optional
from dataclasses import dataclass


@dataclass
class QueueNode:
	value: Any
	following: "QueueNode"


class Queue:

	def __init__(self, elements: Optional[list[Any]]):
		
		self.head = None
		self.end = None
		self.size = 0
		
		if elements:
			for element in elements:
				self.enqueue(element)


	def enqueue(self, element):
		
		newNode = QueueNode(element, following=None)

		if not self.head:
			self.head = newNode
			self.end = newNode
		else:
			self.end.following = newNode
			self.end = newNode

		self.size += 1

	def dequeue(self) -> Optional[Any]:
		if not self.head:
			return None

		temp = self.head
		self.head = self.head.following
		self.size -= 1

		return temp.value

	def peak_top_and_bottom(self) -> dict[str, Any]:
		return {
			"top": self.head.value,
			"bottom": self.end.value
		}

	def __repr__(self) -> str:
		que = []
		head = self.head

		while head:
			que.append(head.value)
			head = head.following

		return f"{que}"


if __name__ == '__main__':
	"""
	For testing purposes + More code for testing in the test folder/
	"""
	
	from rich.console import Console
	console = Console()
	import random

	elem = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
	random.shuffle(elem)

	queue = Queue(elem)
	console.print(queue)

	queue.enqueue(2999)
	queue.enqueue(4999)
	queue.enqueue(69699)
	queue.enqueue(8929)
	
	console.print(queue)

	console.print(queue.dequeue())
	
	console.print("End at", queue.end)
	console.print("stack now:", queue)
	console.print(queue.peak_top_and_bottom())