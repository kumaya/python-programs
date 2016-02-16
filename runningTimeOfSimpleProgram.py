# Program tries to identify the runtime of creating a list using four different ways
import timeit
from timeit import Timer


# create list using concatination
def test1():
    l = []
    for i in range(3000):
        l = l + [i]


# create list using append
def test2():
    l = []
    for i in range(3000):
        l.append(i)


# create list using list comprehension
def test3():
    l = [i for i in range(3000)]


# create list using concat and generator
def test4():
    l = []
    for i in xrange(3000):
        l = l + [i]


# create list using list range
def test5():
    l = list(range(3000))


# create list using list xrange
def test6():
    l = list(xrange(3000))


t1 = Timer("test1()", "from __main__ import test1")
print "time taken using concatination: ", t1.timeit(number=1000), "ms"

t2 = Timer("test2()", "from __main__ import test2")
print "time taken using append: ", t2.timeit(number=1000), "ms"

t3 = Timer("test3()", "from __main__ import test3")
print "time taken using comprehension: ", t3.timeit(number=1000), "ms"

t4 = Timer("test4()", "from __main__ import test4")
print "time taken using concatination and xrange: ", t4.timeit(number=1000), "ms"

t5 = Timer("test5()", "from __main__ import test5")
print "time taken using list range: ", t5.timeit(number=1000), "ms"

t6 = Timer("test6()", "from __main__ import test6")
print "time taken using list xrange: ", t6.timeit(number=1000), "ms"
