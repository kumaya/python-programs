# Method resolution order

# Old styled class mro
class foo():
    a = "foo"

class bar(foo):
    pass

class baz(foo):
    a = "baz"

class derived(bar, baz):
    pass

instance = derived()
print instance.a


# New styled class
class foo(object):
    a = "foo"

class bar(foo):
    pass

class baz(foo):
    a = "baz"

class derived(bar, baz):
    pass

instance = derived()
print instance.a
print derived.__mro__

# impossible method resolution
class x(object):
    a = "x"

class y(object):
    a = "y"

class v(x, y):
    pass

class w(y, x):
    pass

class A(v, w):
    pass

print A.__mro__