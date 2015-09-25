# Linked list using property as setter and getter


class Node(object):
    @property
    def data(self):
        return self.va

    @data.setter
    def data(self, data=None):
        self.va = data

    @property
    def node(self):
        return self.next_node

    @node.setter
    def node(self, new_next):
        self.next_node = new_next


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def  isEmpty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.node
        return count

    def insert(self, val):
        new_node = Node()
        new_node.data = val
        new_node.node = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node()
        new_node.data = data
        current = self.head
        previous = None
        if not current:
            new_node.node = self.head
            self.head = new_node
        else:
            while current:
                previous = current
                current = current.node
            previous.node = new_node
            new_node.node = None

    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and not found:
            if current.data == data:
                found = True
            else:
                previous = current
                current = current.node
        if not found:
            raise ValueError("Data %s is not present in list" %data)
        if previous is None:
            self.head = current.node
        else:
            previous.node = current.node

    @staticmethod
    def printLinkedList(head):
        current = head
        print "Linked List: ",
        while current:
            print current.data,
            print "-->",
            current = current.node
        print "X"


if __name__ == "__main__":
    ll_obj = LinkedList()
    ll_obj.insert(1)
    ll_obj.insert(2)
    ll_obj.insert(3)
    ll_obj.insert(4)
    ll_obj.insert(12)
    ll_obj.insert_at_end(5)
    ll_obj.printLinkedList(ll_obj.head)
