# return n fibonacci numbers

def fib1():
    x = 0
    y = 1
    while True:
        x, y = y, x+y
        yield x

call = fib1()
l = []
for _ in range(5):
    l.append(call.next())
print "Way 1:", l


def fib2(n):
    x = 0
    y = 1
    for _ in range(n):
        x, y = y, x+y
        yield x

print "Way 2:", list(fib2(5))


class rev_iter():
    '''
    Writing your own iterable
    __iter__ actually returns the iterable
    '''
    def __init__(self, n):
        self.i = 0
        self.n = n

    def __iter__(self):
        return self

    def next(self):
        if self.i < self.n:
            n = self.n
            self.n -= 1
            return n
        else:
            raise StopIteration

ca = rev_iter(5)
print "Own iterable:", ca.next(), ca.next(), ca.next(), ca.next(), ca.next()

# Make this easier using generator
def rev_iter_using_generator(n):
    for _ in range(n):
        yield n
        n -= 1

ca = rev_iter_using_generator(5)
print "Above using generator:", ca.next(), ca.next(), ca.next(), ca.next(), ca.next()

# generator expression like list comprehension
print "List comprehension: ", [x*x for x in range(1, 5)]
print "Generator: ", (x*x for x in range(1, 5))
print "List using generator", list((x*x for x in range(1, 5)))