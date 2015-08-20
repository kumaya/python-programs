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

	def insert(self, data):
		new_node = Node(data)
		new_node.set_next(self.head)
		self.head = new_node

	def middle_element(self):
		ptr1 = self.head
		ptr2 = self.head
		while ptr1:
			ptr1 = ptr1.get_next()
			if ptr1:
				ptr1 = ptr1.get_next()
				ptr2 = ptr2.get_next()
		return ptr2.get_data()

	def size(self):
		current = self.head
		count = 0
		while current:
			count += 1
			current = current.get_next()
		return count



ll_obj = LinkedList()
ll_obj.insert('maya')
ll_obj.insert('kuma')
ll_obj.insert('deep')
ll_obj.insert('raj')
ll_obj.insert('rajan')
ll_obj.insert('bhajan')

def printLL():
	curr = ll_obj.head
	while curr:
	    print curr.get_data(), curr.get_next()
	    curr = curr.get_next()

printLL()
print "*"*80
print "Middle element is: ", ll_obj.middle_element()

print "#"*80

def pairWiseSwap(head):
	if (head == None) or (head.get_next() == None):
		return
	prev = head
	curr = head.get_next()

	head.set_next(curr)

	while True:
		nextP = curr.get_next()
		curr.set_next(prev)
		if (nextP == None) or (nextP.get_next() is None):
			prev.set_next(nextP)
			break
		prev.set_next(nextP.get_next())
		prev = nextP
		curr = prev.get_next()

head = ll_obj.head
pairWiseSwap(head)
printLL()