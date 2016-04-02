# Given a sorted doubly link list and two numbers C and K.
# You need to decrease the info of node with data K by C and
# insert the new node formed at its correct position such that the list remains sorted.


class NodeDLL(object):
    def __init__(self, data):
        self._data = data
        self._pn = None
        self._nn = None

    @property
    def data(self):
        return self._data

    @property
    def prev(self):
        return self._pn

    @prev.setter
    def prev(self, p_node):
        self._pn = p_node

    @property
    def n(self):
        return self._nn

    @n.setter
    def n(self, n_node):
        self._nn = n_node


def printDLL(head):
    while head:
        print head.data, "-->",
        head = head.n


def revDLL(head):
    while head:
        print head.data, "-->",
        head = head.prev


def modify(h, c, k):
    final = h
    data = k - c
    while h:
        if data == h.data:
            break
        if data > h.data:
            h = h.n
        else:
            new_node = NodeDLL(data)
            new_node.n = h
            new_node.prev = h.prev
            if h.prev:
                h.prev.n = new_node
            else:
                final = new_node
            h.prev = new_node
            break
    while h:
        if k == h.data:
            h.prev.n = h.n
            if h.n:
                h.n.prev = h.prev
        h = h.n
    return final


if __name__ == "__main__":
    head = NodeDLL(2)
    head.n = NodeDLL(3)
    head.n.prev = head
    head.n.n = NodeDLL(6)
    head.n.n.prev = head.n
    head.n.n.n = NodeDLL(9)
    head.n.n.n.prev = head.n.n
    head.n.n.n.n = NodeDLL(10)
    head.n.n.n.n.prev = head.n.n.n
    print "Original DLL: ", printDLL(head)
    print "Original Reversed DLL: ", revDLL(head.n.n.n.n)
    k = 9
    c = 5
    nh = modify(head, c, k)
    print "Modified DLL: ", printDLL(nh)
    print "Reversed DLL: ", revDLL(nh.n.n.n.n)