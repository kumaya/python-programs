# Linked list implementation in python

# Basic structure of a node in linked list
class Node(object):
	def __init__(self, data=None, next_node=None):
		self.data = data
		self.next_node = next_node

	def get_data(self):
		return self.data

	def get_next(self):
		return self.next_node

	def set_next(self, new_next):
		self.next_node = new_next

class LinkedList(object):
	def __init__(self, head=None):
		self.head = head

	def  isEmpty(self):
		return self.head == None

	def size(self):
		current = self.head
		count = 0
		while current:
			count += 1
			current = current.get_next()
		return count

	def insert(self, data):
		new_node = Node(data)
		new_node.set_next(self.head)
		self.head = new_node

	def insert_at_end(self, data):
		new_node = Node(data)
		current = self.head
		previous = None
		if not current:
			new_node.set_next(self.head)
			self.head = new_node
		else:
			while current:
				previous = current
				current = current.get_next()
			previous.set_next(new_node)
			new_node.set_next(None)

	def delete(self, data):
		current = self.head
		previous = None
		found = False
		while current and not found:
			if current.get_data() == data:
				found = True
			else:
				previous = current
				current = current.get_next()
		if not found:
			raise ValueError("Data %s is not present in list" %data)
		if previous == None:
			self.head = current.get_next()
		else:
			previous.set_next(current.get_next())

	def printLinkedList(self, head):
		current = head
		print "Linked List: ",
		while current:
			print current.get_data(),
			print "-->",
			current = current.get_next()
		print "X"

if __name__ == "__main__":
	ll_obj = LinkedList()
	ll_obj.insert(1)
	ll_obj.insert(2)
	ll_obj.insert(3)
	ll_obj.insert(4)
	ll_obj.insert_at_end(5)
	ll_obj.printLinkedList(ll_obj.head)