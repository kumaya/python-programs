class foo(object):
    pass

class bar(object):
    __slots__ = ['a', 'b']

print "Evaluation for class foo() ===>"
ob1 = foo()
ob1.a = 1
print "Value of foo().a: ", ob1.a
# print dir(ob1)
print "__dict__ attribute: ", ob1.__dict__

print ""
print "Evaluation for class bar() ===>"
ob2 = bar()
# print dir(ob2)
try:
    print ob2.__dict__
except AttributeError:
    print "bar() does not contain __dict__ attribute"
print "type(__slots__): ", type(ob2.__slots__)
try:
    ob2.c = 3
    print ob2.c
except AttributeError:
    print "Cannot assign attribute 'c' to class because of defined __slots__"
