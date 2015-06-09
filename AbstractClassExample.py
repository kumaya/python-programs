import abc

class AbsBaseClass(object):
	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def input(self, input):
		return

	@abc.abstractmethod
	def output(self, output, data):
		pass

class UseAbsClass(AbsBaseClass):

	def returnSomething(self):
		print "maya"
		return

	def input(self, input):
		return self.returnSomething

	# def output(self, output, data):
	# 	return output.write(data)

objX = UseAbsClass()
objX.returnSomething()
#print dir(objX.input(5))

print type(UseAbsClass)
print type(AbsBaseClass)
print type(abc.ABCMeta)
