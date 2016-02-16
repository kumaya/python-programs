"""
This example shows concept of inheritance in python
"""


# Parent class
class Person(object):
    def speak(self):
        print "I can speak"


# Child class
class Man(Person):
    def wear(self):
        print "I wear shirt"


instanceOfChildClass = Man()
instanceOfChildClass.wear()
instanceOfChildClass.speak()  # speak method is inherited from parent class

print "*" * 80
"""
This example shows concept of multiple inheritance in python
class FromKashmir inherits class Indian as well as class Man.
inheritance is left to right
"""


class Indian(object):
    def wear(self):
        print "I wear sherwani"

    def speak(self):
        print "I speak Hindi"


class FromKashmir(Indian, Man):
    def paradise(self):
        print "Paradise on earth"


instanceOfFromKashmirClass = FromKashmir()
instanceOfFromKashmirClass.paradise()
instanceOfFromKashmirClass.speak()
instanceOfFromKashmirClass.wear()  # Left to right inheritance. method wear of class Indian called

print "*" * 80
"""
Encapsulation in python.
"""


class Test(object):
    def publicMethod(self):
        print "You can see mee"

    def __privateMethod(self):  # Adding '__' in front of method/variable hide them
        print "You cannot see me"


instanceOfTestClass = Test()
instanceOfTestClass.publicMethod()
instanceOfTestClass._Test__privateMethod()  # Nothing is private in python. It is just a rule and not limitation.
# using _ClassName_methodName it can be called so we can't access them
# because of wrong names

print "*" * 80
"""
Polymorphism in python
"""


class Bird(object):
    def name(self):
        pass

    def fly(self):
        print "fly"

    def buildNest(self):
        pass


class Crow(Bird):
    def name(self):
        print "I am a crow"

    def buildNest(self):
        print "I build nest"


class Cuckoo(Bird):
    def name(self):
        print "I am a cuckoo"

    def buildNest(self):
        print "I don't build nests"


class TestBirds(Bird):
    def printName(self, bird):
        bird.name()

    def goFly(self, bird):
        bird.fly()

    def buildNest(self, bird):
        bird.buildNest()


TestBirds = TestBirds()
crow = Crow()
cuckoo = Cuckoo()

TestBirds.printName(crow)
TestBirds.goFly(crow)
TestBirds.buildNest(crow)

TestBirds.printName(cuckoo)
TestBirds.goFly(cuckoo)
TestBirds.buildNest(cuckoo)

print "*" * 80
"""
more Polymorphism
variable can support any object which supports add operation
"""
print 1 + 2
print 'kuch' + 'Bhi'
print [1, 2, 3] + [4, 5, 6]