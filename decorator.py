# def myDecorator(some_func):
#     def myOrigDeco(*args, **kwargs):
#         print "enter function ", some_func.__name__
#         count = 0
#         while count <= 5:
#             count += 1
#             print "***************", count
#             try:
#                 return some_func(*args, **kwargs)
#             except Exception as e:
#                 if count < 5:
#                     import time
#                     time.sleep(2)
#                     continue
#             raise e
#     return myOrigDeco

# @myDecorator
# def sum(a, b):
#     # return a+b
#     raise Exception("ValueError")

# val = sum(3,4)
# print val

print "*"*80

from functools import wraps
import time
def retry(retries=0, delay=0):
    def myDecorator(some_func):
        @wraps(some_func)
        def myOrigDeco(*args, **kwargs):
            """Original decorator function"""
            # print "enter function ", some_func.__name__
            count = 0
            while count <= retries:
                count += 1
                # print "********************************************", count
                try:
                    return some_func(*args, **kwargs)
                except Exception as e:
                    if count <= retries:
                        print("Exception in " + some_func.__name__ + ". " +
                                  "Retry counter: " + str(count))
                        time.sleep(delay)
                        continue
                    raise e
        return myOrigDeco
    return myDecorator

@retry(retries=3, delay=2)
def sum(a,b):
    """ This method adds two number
    @param a: Integer number 01
    @param b: Integer number 02
    @return a+b
    """
    return a+b

val = sum(3,4)
print val, "\n", sum.__name__, "\n", sum.__doc__

print "*"*80

# def decoratorFunctionWithArguments(arg1, arg2, arg3):
#     def wrap(f):
#         print "Inside wrap()"
#         def wrapped_f(*args):
#             print "Inside wrapped_f()"
#             print "Decorator arguments:", arg1, arg2, arg3
#             f(*args)
#             print "After f(*args)"
#         return wrapped_f
#     return wrap

# @decoratorFunctionWithArguments("hello", "world", 42)
# def sayHello(a1, a2, a3, a4):
#     print 'sayHello arguments:', a1, a2, a3, a4

# print "After decoration"

# print "Preparing to call sayHello()"
# sayHello("say", "hello", "argument", "list")
# print "after first sayHello() call"
# sayHello("a", "different", "set of", "arguments")
# print "after second sayHello() call"


# Case 1: where we declare call to testFunc in __call__. Here deco obj is defined at call time itself
# class myDeco(object):
#     def __init__(self, f):
#         print "Inside __init__ of deco"
#         self.f = f
#     def __call__(self):
#         print "Inside __call__ of deco"
#         self.f()
#         print "Exiting __call__"

# @myDeco
# def testFunc():
#     print "Inside testFunc"

# print "Call the testFunc"
# testFunc()

# #case 2:
# print "%"*80
# class myDeco(object):
#     def __init__(self, f):
#         print "Inside __init__ of deco"
#         self.f = f
#         f()
#     def __call__(self):
#         print "Inside __call__ od deco"
#         self.f()
#         print "Exiting __call__"

# # Case 1: where we declare call to testFunc in __call__. Here deco obj is defined at call time itself
# @myDeco
# def testFunc():
#     print "Inside testFunc"

# print "Call the testFunc"
# testFunc()

