# Complete implementation of stack DS in python

class  Stack(object):
	"""Implemenation of stack ADT"""
	def __init__(self):
		self.items = []

	def is_empty(self):
		return self.items == []

	def size(self):
		return len(self.items)

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[self.size() - 1]

