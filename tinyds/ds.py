from typing import Any
from dataclasses import dataclass


@dataclass()
class Node:
	data: Any
	next: 'Node' = None


@dataclass()
class TreeNode:
	data: Any
	left: 'TreeNode' = None
	right: 'TreeNode' = None


def insert_bst(node: TreeNode, root: TreeNode):
	"""
	Insert a node into a BST. Pass root as None to create a BST from start
	Args:
		node: Value/object that you want to add, must be comparable
		root: Root of the BST
	"""
	if root is None:
		root = node
	else:
		if node.data < root.data:
			if root.left is None:
				root.left = node
			else:
				insert_bst(node, root.left)

		if node.data > root.data:
			if root.right is None:
				root.right = node
			else:
				insert_bst(node, root.right)


def isLeaf(node: TreeNode) -> bool:
	"""
	Returns True if a node is a leaf
	Args:
		node: Tree Node as an input
	Returns:
		Boolean: Returns True if a node is a leaf
	"""
	if node.right is None and node.left is None:
		return True
	return False

