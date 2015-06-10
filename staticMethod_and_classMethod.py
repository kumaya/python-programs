# test program for the concept of static method and class method

class parent(object):
	@staticmethod
	def static_method(x):
		print "parent", x

	@classmethod
	def class_method(cls, x):
		print "parent", cls, x

	def normal_method(self, x):
		print "parent", self, x

class child1(parent):
	# def static_method(x):
	# 	print "child1", x

	def class_method(cls, x):
		print "child1", x

	def normal_method(self, x):
		print "child1", self, x

class child2(parent):
	@staticmethod
	def static_method(x):
		print "child2", x

	# @classmethod
	# def class_method(cls, x):
	# 	print "child2", cls, x

	def normal_method(self, x):
		print "child2", self, x

obj_child1 = child1()
obj_child2 = child2()
obj_parent = parent()

obj_child1.normal_method(4)
obj_child2.normal_method(4)
obj_parent.normal_method(4)

# obj_parent.static_method(5)
parent.static_method(5)

child1.static_method(6)

obj_child2.static_method(7)

parent.class_method(8)
# obj_parent.class_method(12)

obj_child1.class_method(8)
child2.class_method(8)

val = child2.class_method(4)
val2 = parent.class_method(4)
print isinstance(val, child2)
print isinstance(val, parent)
print isinstance(val2, parent)
