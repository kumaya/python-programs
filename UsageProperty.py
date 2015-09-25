"""
What @property decorator really is and how it works
"""


class UsagePropertyDeco(object):
    def __init__(self, name_is=None):
        print "Inside __init__"
        self.name = name_is

    def a(self):
        print "inside A: 1"

        def b(msg):
            print "Inside B: 1"
            return msg
        print "Inside A: 2"
        return b

    @property
    def c(self):
        print "Inside C: 1"
        return self.a()


class AlternateToPropertyDeco(object):
    def __init__(self, name_is):
        print "Inside __init__"
        self.name = name_is

    @property
    def a(self):
        print "Getter invoked"
        return self.name

    @a.setter
    def a(self, val):
        print "Setter invoked"
        self.name = val


if __name__ == "__main__":
    name = "Mayank"
    obj = UsagePropertyDeco(name)
    msg = "My name is mayank kumar"
    print obj.c(msg)

    print "*"*80

    obj = AlternateToPropertyDeco(name)
    print obj.a
    obj.a = "maya"
    print obj.a
